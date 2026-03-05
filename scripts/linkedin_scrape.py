#!/usr/bin/env python3
"""
LinkedIn scraper using a saved browser session.

Step 1 — Save session (CLOSE Firefox first, then run):
    python3 linkedin_scrape.py --login

    LinkedIn binds li_at to a browser fingerprint. Close Firefox completely,
    run --login, then immediately scrape before any other LinkedIn use.

Step 2 — Scrape:
    python3 linkedin_scrape.py                                    # your profile (text)
    python3 linkedin_scrape.py --json                             # your profile (JSON)
    python3 linkedin_scrape.py --posts                            # your posts (text)
    python3 linkedin_scrape.py --company eusome-project           # company page posts
    python3 linkedin_scrape.py --company eusome-project --json    # company posts (JSON)
    python3 linkedin_scrape.py --company eusome-project \
        --save-posts ./content/post/eusome                        # save posts + images

    Session cookies are saved after each run so the next run stays valid.
"""

import sys
import json
import time
import re
import hashlib
from pathlib import Path
from playwright.sync_api import sync_playwright

MY_PROFILE_URL  = "https://www.linkedin.com/in/evangelos-vlachos-b543103a/"
MY_FEED_URL     = "https://www.linkedin.com/in/evangelos-vlachos-b543103a/recent-activity/all/"
SESSION_FILE    = Path.home() / ".linkedin_session.json"
FIREFOX_PROFILE = Path.home() / ".mozilla/firefox/4a6nvqq7.default-esr"


def clean(text):
    return re.sub(r'\s+', ' ', text or '').strip()


# Emoji ranges + variation selectors + ZWJ
_EMOJI_RE = re.compile(
    '['
    '\U0001F100-\U0001FFFF'
    '\U00002600-\U000027BF'
    '\U0000FE00-\U0000FE0F'
    '\u200D\u20E3'
    ']+',
    flags=re.UNICODE,
)
_HASHTAG_RE = re.compile(r'\s*#[A-Za-z]\w*')


def clean_text(text):
    """Remove emoji and hashtags from scraped LinkedIn text."""
    text = _EMOJI_RE.sub('', text or '')
    text = _HASHTAG_RE.sub('', text)
    text = re.sub(r'  +', ' ', text)
    return text.strip()


# ── Step 1: extract cookies from Firefox ─────────────────────────────────────
def save_session():
    """Extract LinkedIn cookies directly from Firefox's SQLite cookie store."""
    import sqlite3, shutil, tempfile

    cookies_db = FIREFOX_PROFILE / "cookies.sqlite"
    if not cookies_db.exists():
        print(f"Cookies DB not found at {cookies_db}", file=sys.stderr)
        sys.exit(1)

    with tempfile.NamedTemporaryFile(suffix=".sqlite", delete=False) as tmp:
        tmp_path = tmp.name
    shutil.copy2(cookies_db, tmp_path)
    wal = cookies_db.parent / "cookies.sqlite-wal"
    if wal.exists():
        shutil.copy2(wal, tmp_path + "-wal")

    conn = sqlite3.connect(tmp_path)
    try:
        conn.execute("PRAGMA wal_checkpoint(PASSIVE)")
    except Exception:
        pass
    rows = conn.execute("""
        SELECT host, path, name, value, expiry, isSecure, isHttpOnly, sameSite
        FROM moz_cookies
        WHERE host LIKE '%linkedin.com%'
    """).fetchall()
    conn.close()
    Path(tmp_path).unlink(missing_ok=True)

    if not rows:
        print("No LinkedIn cookies found — are you logged in to LinkedIn in Firefox?", file=sys.stderr)
        sys.exit(1)

    same_site_map = {0: "None", 1: "Lax", 2: "Strict"}
    cookies = []
    for host, path, name, value, expiry, secure, http_only, same_site in rows:
        cookies.append({
            "name": name,
            "value": value,
            "domain": host,
            "path": path,
            "expires": expiry,
            "httpOnly": bool(http_only),
            "secure": bool(secure),
            "sameSite": same_site_map.get(same_site, "None"),
        })

    SESSION_FILE.write_text(json.dumps({"cookies": cookies, "origins": []}, indent=2))
    li_at = next((c for c in cookies if c["name"] == "li_at"), None)
    if not li_at:
        print("⚠ li_at MISSING — login to LinkedIn in Firefox, close Firefox, retry.", file=sys.stderr)
        sys.exit(1)
    print(f"✓ Extracted {len(cookies)} LinkedIn cookies → {SESSION_FILE}")


# ── Step 2: shared browser setup ─────────────────────────────────────────────
def _make_context(p):
    if not SESSION_FILE.exists():
        print("No session found. Run with --login first.", file=sys.stderr)
        sys.exit(1)
    browser = p.firefox.launch(headless=True)
    ctx = browser.new_context(
        viewport={"width": 1280, "height": 900},
        locale="en-US",
    )
    session = json.loads(SESSION_FILE.read_text())
    ctx.add_cookies(session["cookies"])
    return ctx


def _save_cookies(ctx):
    """Save rotated cookies back to SESSION_FILE (only when li_at is present)."""
    try:
        cookies = ctx.cookies()
        if any(c["name"] == "li_at" for c in cookies):
            SESSION_FILE.write_text(json.dumps({"cookies": cookies, "origins": []}, indent=2))
    except Exception:
        pass


def _navigate(page, url, wait=3):
    from bs4 import BeautifulSoup
    page.goto(url, wait_until="domcontentloaded", timeout=30000)
    time.sleep(wait)
    return BeautifulSoup(page.content(), "html.parser")


def _check_auth(page, ctx):
    if "authwall" in page.url or "/login" in page.url:
        ctx.browser.close()
        print("Session invalid. Close Firefox, run --login, and try again.", file=sys.stderr)
        sys.exit(1)


# ── Profile scraping ──────────────────────────────────────────────────────────
def _extract_section(soup, keyword):
    items = []
    for section in soup.select("section.artdeco-card"):
        h2 = section.find("h2")
        if not h2 or keyword not in h2.get_text().lower():
            continue
        for li in section.select("li.artdeco-list__item"):
            t1 = li.select_one(".t-bold span[aria-hidden='true'], h3")
            t2 = li.select_one(".t-normal:not(.t-black--light) span[aria-hidden='true'], h4")
            t3 = li.select_one(".t-black--light span[aria-hidden='true']")
            if t1:
                items.append({
                    "primary":   clean(t1.text),
                    "secondary": clean(t2.text) if t2 else None,
                    "meta":      clean(t3.text) if t3 else None,
                })
    return items


def scrape_profile():
    with sync_playwright() as p:
        ctx = _make_context(p)
        page = ctx.new_page()

        print("Loading profile...", file=sys.stderr)
        soup_main = _navigate(page, MY_PROFILE_URL, wait=3)
        print(f"  URL: {page.url}", file=sys.stderr)
        _check_auth(page, ctx)
        _save_cookies(ctx)  # capture rotated li_at immediately after auth

        print("Loading experience...", file=sys.stderr)
        soup_exp = _navigate(page, MY_PROFILE_URL + "details/experience/", wait=3)
        print("Loading education...", file=sys.stderr)
        soup_edu = _navigate(page, MY_PROFILE_URL + "details/education/", wait=3)
        print("Loading publications...", file=sys.stderr)
        soup_pub = _navigate(page, MY_PROFILE_URL + "details/publications/", wait=3)

        ctx.browser.close()

    data = {}
    name_el     = soup_main.select_one("h1")
    headline_el = soup_main.select_one(".text-body-medium.break-words")
    about_el    = soup_main.select_one("div.display-flex.ph5.pv3 span[aria-hidden='true']")

    data["name"]     = clean(name_el.text)     if name_el     else None
    data["headline"] = clean(headline_el.text) if headline_el else None
    data["about"]    = clean(about_el.text)    if about_el    else None

    data["experience"]   = _extract_section(soup_exp,  "experience")
    data["education"]    = _extract_section(soup_edu,  "education")
    data["skills"]       = _extract_section(soup_main, "skill")
    data["publications"] = _extract_section(soup_pub,  "publication")

    return data


# ── Image downloading ─────────────────────────────────────────────────────────
def _download_image(ctx, url, dest_path):
    """Download a LinkedIn CDN image using the authenticated request context."""
    try:
        resp = ctx.request.get(url, timeout=15000)
        if resp.ok:
            dest_path.write_bytes(resp.body())
            return True
    except Exception as e:
        print(f"  ⚠ image download failed: {e}", file=sys.stderr)
    return False


def _extract_post_images(page, post_selector):
    """Return list of image src URLs from each post container via JS evaluation."""
    return page.evaluate(f"""
        () => {{
            const results = [];
            const posts = document.querySelectorAll('{post_selector}');
            posts.forEach(post => {{
                const imgs = [];
                // Try all img tags inside the post
                post.querySelectorAll('img').forEach(img => {{
                    const src = img.getAttribute('src') || img.getAttribute('data-delayed-url') || '';
                    // Filter: only LinkedIn media CDN images, skip avatars/icons
                    if (src.includes('media.licdn.com') || src.includes('media-exp')) {{
                        // Skip tiny images (avatars are usually < 100px)
                        const w = img.naturalWidth || img.width || 0;
                        const h = img.naturalHeight || img.height || 0;
                        if (w > 100 || h > 100 || (w === 0 && h === 0)) {{
                            if (!imgs.includes(src)) imgs.push(src);
                        }}
                    }}
                }});
                results.push(imgs);
            }});
            return results;
        }}
    """)


# ── Post scraping (personal feed or company page) ─────────────────────────────
def _scrape_posts_from_url(feed_url, max_scroll=10, image_dir=None):
    from bs4 import BeautifulSoup

    with sync_playwright() as p:
        ctx = _make_context(p)
        page = ctx.new_page()
        print(f"Loading posts from {feed_url} ...", file=sys.stderr)
        _navigate(page, feed_url, wait=3)
        print(f"  URL: {page.url}", file=sys.stderr)
        _check_auth(page, ctx)
        _save_cookies(ctx)

        for _ in range(max_scroll):
            page.evaluate("window.scrollBy(0, 1000)")
            time.sleep(0.8)
        time.sleep(1)

        # Extract image URLs per post while browser is still open
        post_selector = "div.feed-shared-update-v2, div.occludable-update"
        try:
            img_lists = _extract_post_images(page, "div.feed-shared-update-v2")
        except Exception:
            img_lists = []

        soup = BeautifulSoup(page.content(), "html.parser")
        post_els = soup.select("div.feed-shared-update-v2, div.occludable-update")

        # Download images before closing browser
        downloaded = []  # list of lists of local paths (or None)
        if image_dir:
            image_dir = Path(image_dir)
            image_dir.mkdir(parents=True, exist_ok=True)
            for i, img_urls in enumerate(img_lists):
                post_imgs = []
                for j, url in enumerate(img_urls[:4]):  # cap at 4 images per post
                    ext = ".jpg"
                    if ".png" in url: ext = ".png"
                    elif ".gif" in url: ext = ".gif"
                    fname = f"post_{i:03d}_img{j}{ext}"
                    dest = image_dir / fname
                    if not dest.exists():
                        ok = _download_image(ctx, url, dest)
                        if ok:
                            print(f"  ↓ {fname}", file=sys.stderr)
                    if dest.exists():
                        post_imgs.append(str(dest))
                downloaded.append(post_imgs)

        ctx.browser.close()

    # Pair text/date with downloaded images
    posts = []
    seen = set()
    img_idx = 0
    for el in post_els:
        text_el = el.select_one("div.feed-shared-text span[dir='ltr'], "
                                 "div.update-components-text span[dir='ltr']")
        date_el = el.select_one("time, span.update-components-actor__sub-description")
        text = clean_text(clean(text_el.text)) if text_el else None
        if not text or text[:60] in seen:
            img_idx += 1
            continue
        seen.add(text[:60])
        post = {
            "text": text,
            "date": clean(date_el.text) if date_el else None,
            "images": downloaded[img_idx] if image_dir and img_idx < len(downloaded) else [],
        }
        img_idx += 1
        posts.append(post)
    return posts


def scrape_my_posts(max_scroll=10, image_dir=None):
    return _scrape_posts_from_url(MY_FEED_URL, max_scroll, image_dir)


def scrape_company_posts(company_slug, max_scroll=10, image_dir=None):
    """Scrape recent posts from a LinkedIn company/project page."""
    url = f"https://www.linkedin.com/company/{company_slug}/posts/"
    return _scrape_posts_from_url(url, max_scroll, image_dir)


# ── CLI ───────────────────────────────────────────────────────────────────────
def _arg(flag):
    """Return value after flag in sys.argv, or None."""
    try:
        return sys.argv[sys.argv.index(flag) + 1]
    except (ValueError, IndexError):
        return None


if __name__ == "__main__":
    if "--login" in sys.argv:
        save_session()
        sys.exit(0)

    as_json      = "--json"    in sys.argv
    get_posts    = "--posts"   in sys.argv
    company_slug = _arg("--company")
    image_dir    = _arg("--images")   # download images to this dir

    if company_slug:
        result = scrape_company_posts(company_slug, image_dir=image_dir)
        if as_json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(f"\n{len(result)} posts from '{company_slug}':\n")
            for i, post in enumerate(result, 1):
                imgs = f"  [{len(post['images'])} image(s)]" if post.get("images") else ""
                print(f"[{i}] {post['date']}{imgs}")
                print(f"    {post['text'][:200]}...")
                print()
    elif get_posts:
        result = scrape_my_posts(image_dir=image_dir)
        if as_json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(f"\n{len(result)} posts found:\n")
            for i, post in enumerate(result, 1):
                imgs = f"  [{len(post['images'])} image(s)]" if post.get("images") else ""
                print(f"[{i}] {post['date']}{imgs}")
                print(f"    {post['text'][:200]}...")
                print()
    else:
        result = scrape_profile()
        if as_json:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(f"\nName:     {result.get('name')}")
            print(f"Headline: {result.get('headline')}")
            print(f"\nAbout:\n  {result.get('about')}")
            print(f"\nExperience ({len(result['experience'])}):")
            for e in result["experience"]:
                print(f"  • {e['primary']} @ {e['secondary']} ({e['meta']})")
            print(f"\nEducation ({len(result['education'])}):")
            for e in result["education"]:
                print(f"  • {e['primary']} — {e['secondary']}")
            print(f"\nPublications ({len(result['publications'])}):")
            for pub in result["publications"]:
                print(f"  • {pub['primary']}")
