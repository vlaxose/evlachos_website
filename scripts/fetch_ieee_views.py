#!/usr/bin/env python3
"""
Scrape total download counts from IEEE Xplore for all publications
that have a 10.1109/ DOI. Saves results to data/ieee_views.yaml
so Hugo can embed them in the citation listing.

Usage:  python3 scripts/fetch_ieee_views.py
"""

import os, re, time, yaml, requests
from pathlib import Path

SITE_ROOT   = Path(__file__).parent.parent
PUB_DIR     = SITE_ROOT / "content" / "publication"
OUTPUT_FILE = SITE_ROOT / "data" / "ieee_views.yaml"

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


def get_article_number(doi: str) -> str | None:
    """Follow doi.org redirect → extract IEEE article number from URL."""
    try:
        r = requests.get(
            f"https://doi.org/{doi}",
            headers={"User-Agent": HEADERS["User-Agent"]},
            allow_redirects=True,
            timeout=10,
        )
        m = re.search(r"ieeexplore\.ieee\.org/document/(\d+)", r.url)
        return m.group(1) if m else None
    except Exception as e:
        print(f"  [warn] DOI redirect failed for {doi}: {e}")
        return None


def get_downloads(article_number: str) -> int | None:
    """Fetch total download count from IEEE Xplore metrics API."""
    try:
        r = requests.get(
            f"https://ieeexplore.ieee.org/rest/document/{article_number}/metrics",
            headers=HEADERS,
            timeout=10,
        )
        if r.status_code == 200:
            data = r.json()
            return data.get("metrics", {}).get("totalDownloads")
    except Exception as e:
        print(f"  [warn] metrics fetch failed for article {article_number}: {e}")
    return None


def main():
    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    # Load existing data to avoid re-fetching
    existing = {}
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

        doi = m.group(1)
        slug = pub_path.name

        if slug in results:
            print(f"  [skip] {slug} — already cached ({results[slug]} downloads)")
            continue

        print(f"  {slug}")
        print(f"    DOI: {doi}")

        article_num = get_article_number(doi)
        if not article_num:
            print(f"    → could not resolve article number")
            results[slug] = None
            time.sleep(1)
            continue

        print(f"    article: {article_num}")
        time.sleep(0.5)  # be polite

        downloads = get_downloads(article_num)
        print(f"    downloads: {downloads}")
        results[slug] = downloads
        time.sleep(1.0)

    with open(OUTPUT_FILE, "w") as f:
        yaml.dump(results, f, default_flow_style=False, allow_unicode=True)

    print(f"\nSaved {len(results)} entries to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
