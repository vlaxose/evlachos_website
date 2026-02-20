#!/usr/bin/env python3
"""
Fetch IEEE Xplore statistics for all publications with 10.1109/ DOIs.

For each paper the IEEE metrics endpoint returns:
  • Total downloads (all time)
  • WoS + Scopus citation counts
  • Per-year monthly download history  (the "biblio" array)

This script:
  1. Pulls all of the above in a single API call per paper.
  2. Writes a rich data/ieee_stats.yaml usable by Hugo.
  3. Generates a compact sparkline PNG next to each publication's index.md
     (content/publication/<slug>/sparkline.png) so Hugo can expose it as a
     page resource.

Usage:
    python3 scripts/fetch_ieee_stats.py           # skip already-cached slugs
    python3 scripts/fetch_ieee_stats.py --force   # re-fetch & re-render all
"""

import argparse
import re
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import requests
import yaml

# ── Paths ─────────────────────────────────────────────────────────────────────
SITE_ROOT   = Path(__file__).resolve().parent.parent
PUB_DIR     = SITE_ROOT / "content" / "publication"
OUTPUT_FILE = SITE_ROOT / "data" / "ieee_stats.yaml"

# ── Request headers ────────────────────────────────────────────────────────────
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) "
        "Gecko/20100101 Firefox/121.0"
    ),
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://ieeexplore.ieee.org/",
    "X-Requested-With": "XMLHttpRequest",
}

DOI_RE = re.compile(r'doi:\s*"?(10\.1109/[^"\s]+)"?', re.IGNORECASE)

# ── Sparkline style (matches site palette) ─────────────────────────────────────
MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
LINE_COLOR  = "#1a3a5c"
FILL_ALPHA  = 0.20
SPARK_W     = 1.8   # inches
SPARK_H     = 0.45  # inches
SPARK_DPI   = 90


# ── IEEE helpers ───────────────────────────────────────────────────────────────

def get_article_number(doi: str) -> str | None:
    """Follow doi.org redirect and extract the IEEE article number."""
    try:
        r = requests.get(
            f"https://doi.org/{doi}",
            headers={"User-Agent": HEADERS["User-Agent"]},
            allow_redirects=True,
            timeout=12,
        )
        m = re.search(r"ieeexplore\.ieee\.org/document/(\d+)", r.url)
        return m.group(1) if m else None
    except Exception as e:
        print(f"    [warn] DOI redirect failed: {e}")
        return None


def fetch_metrics(article_number: str) -> dict:
    """
    Call the IEEE metrics endpoint and return a structured dict:
      {
        "total_downloads": int,
        "wos_citations":   int | None,
        "scopus_citations":int | None,
        "yearly":          {year_int: downloads_int, ...}   # may be {}
      }
    """
    result = {
        "total_downloads": None,
        "wos_citations":   None,
        "scopus_citations": None,
        "yearly": {},
    }
    try:
        r = requests.get(
            f"https://ieeexplore.ieee.org/rest/document/{article_number}/metrics",
            headers=HEADERS,
            timeout=12,
        )
        if r.status_code != 200:
            print(f"    [warn] metrics HTTP {r.status_code}")
            return result

        data = r.json()
        m = data.get("metrics", {})

        result["total_downloads"]  = m.get("totalDownloads")
        result["wos_citations"]    = m.get("wosCitationCount")
        raw_scopus = m.get("scopus_count")
        if raw_scopus is not None:
            try:
                result["scopus_citations"] = int(raw_scopus)
            except (ValueError, TypeError):
                pass

        # ── Per-year downloads from biblio array ──────────────────────────
        yearly: dict[int, int] = {}
        for entry in m.get("biblio", []):
            try:
                year = int(entry["year"])
            except (KeyError, ValueError, TypeError):
                continue
            total = 0
            for mon in MONTHS:
                val = entry.get(mon, "-")
                if val and val != "-":
                    try:
                        total += int(val)
                    except (ValueError, TypeError):
                        pass
            if total > 0:
                yearly[year] = total

        result["yearly"] = dict(sorted(yearly.items()))

    except Exception as e:
        print(f"    [warn] metrics fetch failed: {e}")

    return result


# ── Sparkline ──────────────────────────────────────────────────────────────────

def make_sparkline(yearly: dict[int, int], out_path: Path) -> bool:
    """
    Render a compact sparkline (cumulative downloads over years) and save it
    as a transparent PNG next to the publication's index.md.
    Returns True on success.
    """
    if not yearly or len(yearly) < 2:
        return False

    years = sorted(yearly.keys())
    per_year = [yearly[y] for y in years]
    cumulative = list(np.cumsum(per_year))

    fig, ax = plt.subplots(figsize=(SPARK_W, SPARK_H))
    fig.patch.set_alpha(0.0)
    ax.set_facecolor("none")

    xs = list(range(len(years)))
    ax.plot(xs, cumulative, color=LINE_COLOR, linewidth=1.4,
            solid_capstyle="round", solid_joinstyle="round")
    ax.fill_between(xs, cumulative, alpha=FILL_ALPHA, color=LINE_COLOR)

    # Dot on the last point
    ax.scatter([xs[-1]], [cumulative[-1]], color=LINE_COLOR, s=12, zorder=3)

    ax.set_xlim(-0.2, len(years) - 0.8)
    ax.set_ylim(0, max(cumulative) * 1.2)
    ax.axis("off")

    fig.tight_layout(pad=0)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        out_path,
        dpi=SPARK_DPI,
        transparent=True,
        bbox_inches="tight",
        pad_inches=0.01,
    )
    plt.close(fig)
    return True


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Fetch IEEE Xplore stats + sparklines")
    parser.add_argument("--force", action="store_true",
                        help="Re-fetch and re-render even cached slugs")
    args = parser.parse_args()

    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    existing: dict = {}
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE) as f:
            existing = yaml.safe_load(f) or {}

    results = dict(existing)
    pub_dirs = sorted(PUB_DIR.iterdir())

    for pub_path in pub_dirs:
        index_md = pub_path / "index.md"
        if not index_md.exists():
            continue

        content = index_md.read_text()
        m = DOI_RE.search(content)
        if not m:
            continue

        doi  = m.group(1)
        slug = pub_path.name
        spark_path = pub_path / "sparkline.png"

        if not args.force and slug in results and spark_path.exists():
            td = (results[slug] or {}).get("total_downloads", "?")
            print(f"  [skip] {slug}  ({td} dl)")
            continue

        print(f"\n  {slug}")
        print(f"    doi: {doi}")

        article_num = get_article_number(doi)
        if not article_num:
            print(f"    → could not resolve article number")
            results[slug] = None
            time.sleep(1)
            continue

        print(f"    article: {article_num}")
        time.sleep(0.5)

        stats = fetch_metrics(article_num)
        print(f"    downloads : {stats['total_downloads']}")
        print(f"    wos cites : {stats['wos_citations']}")
        print(f"    scopus    : {stats['scopus_citations']}")
        print(f"    yearly pts: {len(stats['yearly'])}")

        results[slug] = {
            "total_downloads":  stats["total_downloads"],
            "wos_citations":    stats["wos_citations"],
            "scopus_citations": stats["scopus_citations"],
            "yearly":           stats["yearly"] or None,
        }

        # Generate sparkline
        if stats["yearly"]:
            ok = make_sparkline(stats["yearly"], spark_path)
            print(f"    sparkline : {'saved' if ok else 'skipped (too few points)'}")
        else:
            print(f"    sparkline : skipped (no yearly data)")

        time.sleep(1.0)

    with open(OUTPUT_FILE, "w") as f:
        yaml.dump(results, f, default_flow_style=False, allow_unicode=True,
                  sort_keys=True)

    print(f"\n✓ Saved {len(results)} entries → {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
