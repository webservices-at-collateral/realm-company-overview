"""Join one deck folder into a single static HTML page for a local preview or screenshot.

Usage (from the repo root):
    python scripts/preview_deck.py decks/v1.4-company-overview out/v1.4
    # optional: FONTS_DIR=/path/to/fonts  (Sentient-Variable.woff2, Geist-VariableFont_wght.ttf)
    # optional: ONLY=cover,overview        (render only these slide ids)

Images referenced as /_blob/<id> in the slides resolve through assets/blobs.json.
Then screenshot, e.g. with Edge or Chrome headless:
    msedge --headless=new --window-size=1920,<1080 x slides> --screenshot=out/v1.4/shot.png out/v1.4/index.html
"""
import os, re, sys, json, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
deck_dir, outdir = sys.argv[1], sys.argv[2]
os.makedirs(outdir, exist_ok=True)
blobs = json.load(open(os.path.join(ROOT, "assets", "blobs.json")))
fonts_dir = os.environ.get("FONTS_DIR", os.path.join(ROOT, "fonts"))
deck = json.load(open(os.path.join(deck_dir, "project", "deck.json"), encoding="utf-8"))
only = os.environ.get("ONLY")
if only:
    deck["order"] = [s for s in deck["order"] if s in only.split(",")]


def resolve(bid):
    v = blobs.get(bid)
    if not v:
        return None
    src = os.path.join(fonts_dir, v[5:]) if v.startswith("FONT:") else os.path.join(ROOT, v)
    if not os.path.exists(src):
        return None
    name = bid + os.path.splitext(src)[1]
    shutil.copy(src, os.path.join(outdir, name))
    return name


def fix(text):
    return re.sub(r"/_blob/([0-9a-f]{32})", lambda m: resolve(m.group(1)) or m.group(0), text)


base = """* { margin: 0 }
body { font: 32px/1.2 sans-serif; background: #777 }
body > section { width: 1920px !important; height: 1080px !important; overflow: hidden !important; box-sizing: border-box !important; position: relative; isolation: isolate }
aside { display: none !important }
h1 { font-size: 96px; font-weight: 600 } h2 { font-size: 64px; font-weight: 600 } h3 { font-size: 44px; font-weight: 600 }
.win, .win-vec, .tangent, .bleed-r, .case-ph-r, .case-ph-l, .venn, .ring, .vec, .tex-band, .window-left, .window-vec, .wire, .rings, .g-host, .backdrop, .cyc-ring { z-index: -1 }
.tex-band { z-index: -2 !important }
"""
faces = "".join(
    f"@font-face {{ font-family: '{f['family']}'; src: url({fix(f['src'])}); font-weight: 100 900; }}\n"
    for f in deck["faces"].values() if "src" in f
)
css = fix(open(os.path.join(deck_dir, "project", "deck.css"), encoding="utf-8").read())
slides = "\n".join(
    fix(open(os.path.join(deck_dir, "project", "slides", sid + ".html"), encoding="utf-8").read())
    for sid in deck["order"] if os.path.exists(os.path.join(deck_dir, "project", "slides", sid + ".html"))
)
html = f"<!doctype html><html><head><meta charset='utf-8'><style>{base}{faces}{css}</style></head><body>{slides}</body></html>"
open(os.path.join(outdir, "index.html"), "w", encoding="utf-8").write(html)
print(f"{len(deck['order'])} slides -> {os.path.join(outdir, 'index.html')}")
