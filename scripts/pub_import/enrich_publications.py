#!/usr/bin/env python3
"""
enrich_publications.py

Automatically enrich Hugo publication pages with figures and AI-generated
insights, using a local Ollama model (text-only).

Figures are extracted from the PDF and saved to the publication folder.
Figure captions are parsed from the PDF text and passed to the model as
context, since the local model does not support vision.

Usage (from the repo root):
    scripts/venv/bin/python scripts/pub_import/enrich_publications.py
    scripts/venv/bin/python scripts/pub_import/enrich_publications.py --slug vlachos-turning-2025
    scripts/venv/bin/python scripts/pub_import/enrich_publications.py --force

Requirements (in scripts/venv):
    pip install pillow
System deps (already installed):
    pdftotext, pdfimages   (poppler-utils)
Ollama must be running locally on port 11434.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import urllib.error
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow not found. Run: scripts/venv/bin/pip install pillow")

# ── Config ────────────────────────────────────────────────────────────────────

PUBLICATION_DIR = Path("content/publication")
OLLAMA_URL      = "http://localhost:11434/api/chat"
MODEL           = "deepseek-r1:8b"

MAX_FIGURES     = 5      # figures saved per paper
MIN_FIG_W       = 200    # px – discard images narrower than this
MIN_FIG_H       = 150    # px – discard images shorter than this
MIN_STDEV       = 5.0    # grayscale std-dev – discard near-uniform images (blank/solid)
MAX_MEAN        = 251    # grayscale mean – discard near-white images (blank pages)
MIN_MEAN        = 5      # grayscale mean – discard near-black images
MIN_ASPECT      = 0.25   # w/h – discard extreme portrait strips
MAX_ASPECT      = 6.0    # w/h – discard extreme landscape banners
MAX_AREA        = 7_000_000  # px² – discard full-page scans (A4@300dpi ≈ 8.7M)
MAX_TEXT_CHARS  = 4_000  # chars sent to the model (~1000 tokens; keep well inside num_ctx)

# Page-rendering fallback (used when pdfimages finds no raster content i.e. vector PDFs)
RENDER_DPI      = 150    # DPI for pdftoppm page renders
WHITE_THRESH    = 250    # pixel value ≥ this counts as "white"
WHITE_ROW_PCT   = 0.97   # fraction of row pixels that must be white to call it a white row
MIN_GAP_ROWS    = 10     # consecutive white rows needed to split content blocks
MIN_CROP_H      = 80     # minimum crop height in pixels at RENDER_DPI
MAX_CROP_H_PCT  = 0.72   # discard blocks taller than this fraction of the page (text columns)

OLLAMA_TIMEOUT  = 120    # seconds between streamed chunks (not total response)
OLLAMA_RETRIES  = 2      # retry attempts on timeout/error
OLLAMA_NUM_CTX  = 8192   # context window tokens (overrides model default of 4096)

# ── Text helpers ──────────────────────────────────────────────────────────────

def extract_text(pdf: Path) -> str:
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf), "-"],
        capture_output=True, text=True
    )
    return result.stdout


def smart_truncate(text: str, limit: int) -> str:
    """Keep intro + results/conclusion within the char budget."""
    if len(text) <= limit:
        return text

    half = limit // 2
    head = text[:half]

    ref_match  = re.search(r'\bREFERENCES\b', text, re.IGNORECASE)
    tail_end   = ref_match.start() if ref_match else len(text)
    tail_start = max(half, tail_end - half)
    tail       = text[tail_start:tail_end]

    return head + "\n\n[...middle of paper omitted...]\n\n" + tail


def extract_figure_captions(text: str) -> dict[int, str]:
    """
    Parse figure captions from the raw PDF text.
    Matches patterns like 'Fig. 3:', 'Figure 3.', 'FIG. 3 —'.
    Returns {figure_number: caption_text}.
    """
    captions: dict[int, str] = {}
    pattern = re.compile(
        r'\bFig(?:ure)?\.?\s*(\d{1,2})[:\.\s\u2013\u2014\-]+([^\n]{15,250})',
        re.IGNORECASE
    )
    for m in pattern.finditer(text):
        num     = int(m.group(1))
        caption = m.group(2).strip().rstrip('.')
        if num not in captions:          # keep first occurrence
            captions[num] = caption
    return captions

# ── Figure helpers ────────────────────────────────────────────────────────────

def _image_stats(img: Image.Image) -> tuple[float, float]:
    """Return (mean, stdev) of grayscale pixel values."""
    gray = img.convert("L")
    pixels = list(gray.tobytes())
    mean = sum(pixels) / len(pixels)
    stdev = (sum((p - mean) ** 2 for p in pixels) / len(pixels)) ** 0.5
    return mean, stdev


def _is_bad_image(img: Image.Image) -> bool:
    """
    Return True if the image is likely not a scientific figure:
      - Extreme aspect ratio (banner or thin strip)
      - Full-page scan (area too large)
      - Near-white or near-black (blank page or solid fill)
      - Near-uniform (no visible content)
    """
    w, h = img.size
    aspect = w / h

    if aspect > MAX_ASPECT or aspect < MIN_ASPECT:
        return True

    if w * h > MAX_AREA:
        return True

    mean, stdev = _image_stats(img)

    if mean > MAX_MEAN or mean < MIN_MEAN:
        return True

    if stdev < MIN_STDEV:
        return True

    return False


def _crop_figures_from_page(page: Image.Image, out_dir: Path, prefix: str) -> list[Path]:
    """
    Split a rendered page into content blocks separated by wide white-space gaps,
    filter to blocks that look like figures, and save each as a PNG.
    """
    gray = page.convert("L")
    pw, ph = page.size
    raw = gray.tobytes()

    # Mark each row as "white" (≥WHITE_ROW_PCT fraction of pixels above WHITE_THRESH)
    white_row = []
    for y in range(ph):
        row = raw[y * pw:(y + 1) * pw]
        white_row.append(sum(1 for p in row if p >= WHITE_THRESH) / pw >= WHITE_ROW_PCT)

    # Split into blocks separated by ≥MIN_GAP_ROWS consecutive white rows
    blocks: list[tuple[int, int]] = []
    in_block = False
    block_start = 0
    gap = 0
    for y, is_white in enumerate(white_row):
        if not is_white:
            if not in_block:
                block_start = y
                in_block = True
            gap = 0
        else:
            if in_block:
                gap += 1
                if gap >= MIN_GAP_ROWS:
                    blocks.append((block_start, y - gap + 1))
                    in_block = False
                    gap = 0
    if in_block:
        blocks.append((block_start, ph))

    crops: list[Path] = []
    for i, (y0, y1) in enumerate(blocks):
        h = y1 - y0
        if h < MIN_CROP_H or h > ph * MAX_CROP_H_PCT:
            continue
        crop = page.crop((0, y0, pw, y1))
        if _is_bad_image(crop):
            continue
        out = out_dir / f"{prefix}_b{i:02d}.png"
        crop.save(out)
        crops.append(out)
    return crops


def _render_page_figures(pdf: Path, tmpdir: Path) -> list[Path]:
    """
    Fallback for vector-only PDFs: render each page with pdftoppm and
    extract figure-like content blocks via whitespace splitting.
    """
    render_dir = tmpdir / "pages"
    render_dir.mkdir(exist_ok=True)
    r = subprocess.run(
        ["pdftoppm", "-png", "-r", str(RENDER_DPI), str(pdf), str(render_dir / "p")],
        capture_output=True,
    )
    if r.returncode != 0:
        return []

    crops: list[Path] = []
    for page_path in sorted(render_dir.glob("p-*.png")):
        try:
            with Image.open(page_path) as page:
                crops.extend(_crop_figures_from_page(page, tmpdir, page_path.stem))
        except Exception:
            pass
    return crops


def extract_figures(pdf: Path, tmpdir: Path) -> list[Path]:
    """
    Dump all raster images from the PDF, apply quality filters,
    deduplicate, and return up to MAX_FIGURES in document order.
    Falls back to page rendering for vector-only PDFs.
    """
    subprocess.run(
        ["pdfimages", "-png", str(pdf), str(tmpdir / "fig")],
        capture_output=True
    )

    seen: set[tuple[int, int, int]] = set()   # (w, h, rounded_mean) for dedup
    candidates: list[Path] = []

    for img_path in sorted(tmpdir.glob("fig-*.png")):   # sorted = document order
        try:
            with Image.open(img_path) as im:
                w, h = im.size
                if w < MIN_FIG_W or h < MIN_FIG_H:
                    continue
                if _is_bad_image(im):
                    continue
                mean, _ = _image_stats(im)
                key = (w, h, round(mean))
                if key in seen:
                    continue   # likely duplicate image
                seen.add(key)
                candidates.append(img_path)
        except Exception:
            pass

    if not candidates:
        print("      no raster images found — trying page rendering fallback…")
        candidates = _render_page_figures(pdf, tmpdir)
        if candidates:
            print(f"      page rendering yielded {len(candidates)} block(s)")

    return candidates[:MAX_FIGURES]


def strip_ghost_figure_refs(markdown: str, n_saved: int) -> str:
    """
    Remove {{< figure >}} shortcodes whose source files were not actually saved.
    If n_saved == 0, remove the entire Results & Insights section.
    """
    if n_saved == 0:
        markdown = re.sub(
            r'\n*## Results & Insights\b.*',
            '',
            markdown,
            flags=re.DOTALL,
        ).strip()
    else:
        # Remove shortcodes for figure indices beyond n_saved
        for i in range(n_saved + 1, MAX_FIGURES + 5):
            markdown = re.sub(
                r'\{\{<\s*figure\s+src="fig' + str(i) + r'\.png"[^}]*>\}\}\n+[^\n]*\n*',
                '',
                markdown,
            )
    return markdown.strip()

# ── State check ───────────────────────────────────────────────────────────────

def already_enriched(index_md: Path) -> bool:
    content = index_md.read_text()
    parts   = content.split("---", 2)
    return len(parts) >= 3 and bool(parts[2].strip())

# ── Ollama call ───────────────────────────────────────────────────────────────

def _build_prompt(text: str, captions: dict[int, str], title: str, n_figures: int) -> str:
    if n_figures > 0:
        fig_lines = []
        for i in range(1, n_figures + 1):
            cap = captions.get(i, "(caption not found in text)")
            fig_lines.append(f"  fig{i}.png — {cap}")
        fig_block = "Figures saved from the PDF (ordered by prominence):\n" + "\n".join(fig_lines)
    else:
        fig_block = "No figures were extracted from this PDF."

    return f"""You are writing a short enrichment for an academic paper's webpage.

Paper title: {title}

Paper text (possibly truncated):
{text}

{fig_block}

Write the enrichment in clean Markdown using EXACTLY this structure:

## Key Contributions
- (2–4 bullet points summarising the main technical contributions)

## Results & Insights

For each figure whose caption suggests it contains numerical results (performance curves,
BER/NMSE/capacity plots, convergence graphs, comparison tables) write:

{{{{< figure src="figN.png" caption="One precise sentence describing what is plotted." >}}}}

One or two sentences explaining the key takeaway from this figure.

Rules:
- Skip figures whose captions suggest they are block diagrams, system models,
  or signal-flow illustrations with no numerical data.
- If no figures have result-type captions, omit the Results & Insights section.
- Use filenames exactly as listed (fig1.png, fig2.png, …).
- Output ONLY the Markdown body — no preamble, no closing remarks, no code fences.
"""


def call_ollama(text: str, captions: dict[int, str], title: str, n_figures: int) -> str:
    """
    Call Ollama using streaming mode so the per-chunk socket timeout applies
    instead of a single hard deadline for the full response.  deepseek-r1 can
    emit a very long <think> block before answering; streaming avoids timeouts.
    """
    prompt = _build_prompt(text, captions, title, n_figures)

    payload = {
        "model":    MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream":   True,
        "options":  {"temperature": 0.2, "num_ctx": OLLAMA_NUM_CTX},
    }

    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )

    last_error: Exception | None = None
    for attempt in range(1, OLLAMA_RETRIES + 1):
        if attempt > 1:
            print(f"  ↩  retry {attempt}/{OLLAMA_RETRIES}…")
        try:
            chunks: list[str] = []
            with urllib.request.urlopen(req, timeout=OLLAMA_TIMEOUT) as resp:
                for raw_line in resp:
                    line = raw_line.decode().strip()
                    if not line:
                        continue
                    try:
                        obj = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    delta = obj.get("message", {}).get("content", "")
                    if delta:
                        chunks.append(delta)
                    if obj.get("done"):
                        break
            return "".join(chunks).strip()
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last_error = e
            print(f"  ⚠  Ollama timeout/error on attempt {attempt}: {e}")

    raise RuntimeError(
        f"Ollama failed after {OLLAMA_RETRIES} attempt(s): {last_error}"
    )

# ── Per-publication logic ─────────────────────────────────────────────────────

def enrich(pub_dir: Path, force: bool = False):
    index_md = pub_dir / "index.md"
    pdf      = pub_dir / "paper.pdf"

    if not pdf.exists():
        print("  ⏭  no PDF — skip")
        return

    if not force and already_enriched(index_md):
        print("  ⏭  already enriched — skip  (use --force to redo)")
        return

    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)

        print("  📄 extracting text…")
        raw_text = extract_text(pdf)
        text     = smart_truncate(raw_text, MAX_TEXT_CHARS)
        captions = extract_figure_captions(raw_text)

        print("  🖼  extracting figures…")
        fig_paths = extract_figures(pdf, tmpdir)
        print(f"      {len(fig_paths)} figure(s) pass size filter")
        if captions:
            print(f"      {len(captions)} caption(s) found in text")

        # Read title from front-matter
        raw_md  = index_md.read_text()
        m       = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', raw_md, re.MULTILINE)
        title   = m.group(1) if m else pub_dir.name

        print("  🤖 calling Ollama…")
        markdown_body = call_ollama(text, captions, title, len(fig_paths))

        # Remove <think>…</think> reasoning blocks that deepseek-r1 emits
        markdown_body = re.sub(r'<think>.*?</think>', '', markdown_body, flags=re.DOTALL).strip()

        # Copy selected figures into the publication folder
        for i, orig in enumerate(fig_paths):
            shutil.copy(orig, pub_dir / f"fig{i + 1}.png")

        # Remove any figure shortcodes the LLM hallucinated for non-existent files
        markdown_body = strip_ghost_figure_refs(markdown_body, len(fig_paths))

        # Strip old body (handles --force) and write new content
        parts       = raw_md.split("---", 2)
        new_content = "---".join(parts[:2]) + "---\n\n" + markdown_body + "\n"
        index_md.write_text(new_content)

        print(f"  ✅ done  ({len(fig_paths)} figure(s) saved)")

# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Enrich Hugo publication pages with figures and AI insights (local Ollama)."
    )
    parser.add_argument(
        "--slug", metavar="SLUG",
        help="Process only this publication slug (folder name)"
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Re-process publications that already have a body"
    )
    args = parser.parse_args()

    # Sanity-check Ollama is reachable before starting the loop
    try:
        urllib.request.urlopen("http://localhost:11434/", timeout=3)
    except Exception:
        sys.exit("Ollama is not reachable at http://localhost:11434 — is it running?")

    if args.slug:
        targets = [PUBLICATION_DIR / args.slug]
    else:
        targets = sorted(
            p for p in PUBLICATION_DIR.iterdir()
            if p.is_dir() and p.name != "_index.md"
        )

    for pub_dir in targets:
        print(f"\n📚 {pub_dir.name}")
        try:
            enrich(pub_dir, force=args.force)
        except Exception as e:
            print(f"  ❌ error: {e}")

    print("\nAll done.")


if __name__ == "__main__":
    main()
