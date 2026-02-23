#!/usr/bin/env python3
"""
Google Scholar news scraper for Dr. Evangelos Vlachos.

Fetches profile data from Google Scholar and generates Hugo news posts for:
  - New publications recently indexed on Scholar
  - Citation milestones (every 100 citations)
  - h-index improvements

Usage:
    python3 scripts/scholar_news.py                  # check for news
    python3 scripts/scholar_news.py --dry-run        # preview without writing
    python3 scripts/scholar_news.py --milestone-only # only check citation milestones
    python3 scripts/scholar_news.py --profile ID     # override Scholar profile ID
    python3 scripts/scholar_news.py --new-only N     # only report papers from last N years
"""

import argparse
import json
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from textwrap import dedent

# ──────────────────────────────────────────────
# CONFIGURATION
# ──────────────────────────────────────────────
SCHOLAR_PROFILE_ID = "N2ZlmesAAAAJ"   # Dr. Evangelos Vlachos Google Scholar ID

SITE_ROOT  = Path(__file__).resolve().parent.parent
POSTS_DIR  = SITE_ROOT / "content" / "post"
STATE_FILE = Path(__file__).resolve().parent / ".scholar_state.json"

# Milestones to announce (every N citations)
CITATION_MILESTONE_STEP = 100

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("scholar_news")


# ──────────────────────────────────────────────
# STATE
# ──────────────────────────────────────────────

def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            pass
    return {
        "seen_pub_ids": [],
        "last_citation_count": 0,
        "last_hindex": None,   # None = uninitialised; skip h-index post on first run
        "last_run": None,
    }


def save_state(state: dict):
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False))


# ──────────────────────────────────────────────
# HUGO POST HELPERS
# ──────────────────────────────────────────────

def _escape_yaml(text: str) -> str:
    """Escape double quotes for embedding in a YAML double-quoted scalar."""
    return text.replace("\\", "\\\\").replace('"', '\\"')


def _slug(text: str, max_len: int = 80) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower())
    s = re.sub(r"[\s_]+", "-", s).strip("-")
    s = s[:max_len]
    return s.rstrip("-")


def write_post(slug: str, title: str, date_str: str, summary: str,
               tags: list[str], category: str, dry_run: bool = False) -> Path:
    folder = POSTS_DIR / slug
    post_path = folder / "index.md"

    if post_path.exists():
        log.info(f"  ⏭  Post already exists: {slug}")
        return post_path

    tags_yaml = json.dumps(tags)
    content = dedent(f"""\
        ---
        title: "{_escape_yaml(title)}"
        date: {date_str}
        summary: "{_escape_yaml(summary)}"
        tags: {tags_yaml}
        categories: ["{category}"]
        ---

        {summary}
    """)

    if dry_run:
        log.info(f"  [DRY RUN] Would create: {post_path}")
        log.info(f"            Title: {title}")
        log.info(f"            Summary: {summary[:120]}")
        return post_path

    folder.mkdir(parents=True, exist_ok=True)
    post_path.write_text(content, encoding="utf-8")
    log.info(f"  ✨ Created: {post_path.relative_to(SITE_ROOT)}")
    return post_path


# ──────────────────────────────────────────────
# SCHOLAR FETCH
# ──────────────────────────────────────────────

def fetch_author(profile_id: str, use_proxy: bool = False):
    """Return a fully-filled scholarly Author object."""
    from scholarly import scholarly as sc, ProxyGenerator

    if not profile_id:
        raise ValueError(
            "No Scholar profile ID configured.\n"
            "  Find it in your Google Scholar profile URL:\n"
            "    https://scholar.google.com/citations?user=XXXXXXXXX\n"
            "  Then set SCHOLAR_PROFILE_ID in the script or pass --profile XXXXXXXXX"
        )

    if use_proxy:
        log.info("Setting up free proxies (may be slow)…")
        pg = ProxyGenerator()
        pg.FreeProxies()
        sc.use_proxy(pg)

    log.info(f"Fetching Scholar profile: {profile_id}")
    author = sc.search_author_id(profile_id)
    author = sc.fill(author, sections=["basics", "indices", "counts", "publications"])
    return author


def get_publications(author, newer_than_year: int | None = None) -> list[dict]:
    """
    Return publications as plain dicts, optionally filtered to recent ones.
    Each dict has keys: pub_id, title, year, venue, citations, scholar_url.
    """
    pubs = []
    for pub in author.get("publications", []):
        bib   = pub.get("bib", {})
        year  = bib.get("pub_year") or bib.get("year")
        title = bib.get("title", "").strip()
        if not title:
            continue

        try:
            year_int = int(year) if year else 0
        except (ValueError, TypeError):
            year_int = 0

        if newer_than_year and year_int < newer_than_year:
            continue

        pub_id = pub.get("author_pub_id", "").strip()
        if not pub_id:
            # Fallback: derive a stable ID from the title so we can track it
            pub_id = "title:" + re.sub(r"\W+", "-", title.lower())[:60]

        pubs.append({
            "pub_id":      pub_id,
            "title":       title,
            "year":        year_int,
            "venue":       bib.get("journal") or bib.get("booktitle") or bib.get("conference") or "",
            "citations":   pub.get("num_citations", 0),
            "scholar_url": pub.get("pub_url", ""),
        })

    # Newest first
    pubs.sort(key=lambda p: p["year"], reverse=True)
    return pubs


# ──────────────────────────────────────────────
# NEWS GENERATORS
# ──────────────────────────────────────────────

def process_new_publications(author, state: dict, newer_than_year: int | None,
                              dry_run: bool) -> list[str]:
    """Create posts for publications not seen in previous runs."""
    pubs    = get_publications(author, newer_than_year=newer_than_year)
    seen    = set(state.get("seen_pub_ids", []))
    new_seen = set()
    created = []
    today   = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    for pub in pubs:
        pub_id = pub["pub_id"]
        if pub_id in seen:
            continue

        title     = pub["title"]
        year      = pub["year"] or "n/a"
        venue     = pub["venue"]
        venue_str = f" in *{venue}*" if venue else ""

        summary = (
            f'New paper indexed on Google Scholar: "{title}"{venue_str} ({year}). '
            f"Cited {pub['citations']} time(s)."
        )
        tags = ["publication", "research"]
        if "uav" in title.lower() or "unmanned" in title.lower():
            tags.append("UAV")
        if "isac" in title.lower() or "sensing" in title.lower():
            tags.append("ISAC")
        if "6g" in title.lower() or "6 g" in title.lower():
            tags.append("6G")

        slug = _slug(f"new-paper-{title}")
        write_post(slug, f"New Paper: {title}", today, summary, tags, "paper", dry_run)

        new_seen.add(pub_id)
        created.append(title)

    if not dry_run:
        state["seen_pub_ids"] = list(seen | new_seen)
    return created


def process_citation_milestones(author, state: dict, dry_run: bool) -> list[str]:
    """Create a post for every milestone crossed since the last run."""
    total_cites = author.get("citedby", 0) or 0
    prev_cites  = state.get("last_citation_count", 0)
    step        = CITATION_MILESTONE_STEP
    created     = []
    today       = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    prev_milestone = (prev_cites // step) * step
    curr_milestone = (total_cites // step) * step

    # Announce every milestone crossed, not just the highest
    milestone = prev_milestone + step
    while milestone <= curr_milestone:
        title   = f"Reached {milestone}+ Citations on Google Scholar"
        summary = (
            f"The work of Dr. Evangelos Vlachos has now been cited over {milestone} times "
            f"according to Google Scholar (current count: {total_cites})."
        )
        slug = _slug(f"citation-milestone-{milestone}")
        write_post(slug, title, today, summary, ["citations", "milestone"], "milestone", dry_run)
        created.append(title)
        milestone += step

    if not dry_run:
        state["last_citation_count"] = total_cites
    return created


def process_hindex(author, state: dict, dry_run: bool) -> list[str]:
    """Create a post when the h-index improves. Silently initialises on first run."""
    hindex      = author.get("hindex", 0) or 0
    prev_hindex = state.get("last_hindex")   # None on first run
    created     = []
    today       = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if prev_hindex is None:
        # First run — record baseline, no post
        log.info(f"  h-index baseline set to {hindex} (no post on first run)")
    elif hindex > prev_hindex:
        title   = f"h-index Reaches {hindex}"
        summary = (
            f"Dr. Evangelos Vlachos's h-index has increased to {hindex} "
            f"(up from {prev_hindex}), as recorded on Google Scholar."
        )
        slug = _slug(f"hindex-{hindex}")
        write_post(slug, title, today, summary, ["hindex", "milestone"], "milestone", dry_run)
        created.append(title)

    if not dry_run:
        state["last_hindex"] = hindex
    return created


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Scrape Google Scholar for news posts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=dedent("""\
            Examples:
              %(prog)s                         # check everything
              %(prog)s --dry-run               # preview without writing files
              %(prog)s --milestone-only        # only citation/hindex milestones
              %(prog)s --new-only 2024         # only papers from 2024 onward
              %(prog)s --profile SCHOLAR_ID    # override profile ID
              %(prog)s --reset                 # forget previous state
        """),
    )
    parser.add_argument("--profile", default=SCHOLAR_PROFILE_ID,
                        help="Google Scholar author profile ID (the ?user=XXX part of your profile URL)")
    parser.add_argument("--proxy", action="store_true",
                        help="Use free proxies to bypass Scholar rate limiting (slower)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview posts without writing files")
    parser.add_argument("--milestone-only", action="store_true",
                        help="Skip new-publication posts; only check milestones")
    parser.add_argument("--new-only", type=int, default=None, metavar="YEAR",
                        help="Only report publications from YEAR onward (e.g. 2024)")
    parser.add_argument("--reset", action="store_true",
                        help="Clear saved state before running")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    if args.reset and STATE_FILE.exists():
        STATE_FILE.unlink()
        log.info("State reset.")

    state = load_state()

    try:
        author = fetch_author(args.profile, use_proxy=args.proxy)
    except Exception as e:
        log.error(f"Failed to fetch Scholar profile: {e}")
        sys.exit(1)

    name        = author.get("name", "Author")
    total_cites = author.get("citedby", "?")
    hindex      = author.get("hindex", "?")
    i10index    = author.get("i10index", "?")
    pub_count   = len(author.get("publications", []))

    log.info(f"Profile: {name}")
    log.info(f"  Citations: {total_cites}  |  h-index: {hindex}  |  i10: {i10index}  |  Papers: {pub_count}")

    created_all = []

    if not args.milestone_only:
        created = process_new_publications(author, state, args.new_only, args.dry_run)
        created_all.extend(created)
        if created:
            log.info(f"  → {len(created)} new publication post(s)")

    created = process_citation_milestones(author, state, args.dry_run)
    created_all.extend(created)

    created = process_hindex(author, state, args.dry_run)
    created_all.extend(created)

    if not args.dry_run:
        state["last_run"] = datetime.now(timezone.utc).isoformat()
        save_state(state)

    # Summary
    print(f"\n{'═' * 50}")
    print(f"  Scholar: {name}")
    print(f"  Citations: {total_cites}  h-index: {hindex}  i10: {i10index}")
    print(f"  Posts created: {len(created_all)}")
    if created_all:
        for t in created_all:
            print(f"    • {t}")
    if args.dry_run:
        print("  (DRY RUN — no files written)")
    print(f"{'═' * 50}")


if __name__ == "__main__":
    main()
