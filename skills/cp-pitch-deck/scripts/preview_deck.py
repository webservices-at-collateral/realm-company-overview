"""Join a Slides deck folder into one static page for a local headless screenshot.

Usage: python preview_deck.py <deck folder containing project/> <out dir> <blobmap.json: {blob id: local file}>
Optional: ONLY=cover,overview to render a subset. Then e.g.
  msedge --headless=new --virtual-time-budget=15000 --window-size=1920,<1080 x slides> --screenshot=out/shot.png out/index.html
  python sheet.py out/shot.png out/sheet.png <first index> <count>
"""
import sys, os, json, shutil, re

root, outdir, blobmap_path = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(outdir, exist_ok=True)
blobmap = json.load(open(blobmap_path, encoding="utf-8"))
deck = json.load(open(os.path.join(root, "project", "deck.json"), encoding="utf-8"))
ONLY = os.environ.get("ONLY")
if ONLY: deck["order"] = [x for x in deck["order"] if x in ONLY.split(",")]

for bid, src in blobmap.items():
    shutil.copy(src, os.path.join(outdir, bid + os.path.splitext(src)[1]))

def fix(text):
    def rep(m):
        bid = m.group(1)
        return bid + os.path.splitext(blobmap[bid])[1] if bid in blobmap else m.group(0)
    return re.sub(r"/_blob/([0-9a-f]{32})", rep, text)

base = """* { margin: 0 }
body { font: 32px/1.2 sans-serif; background:#777 }
body > section { width: 1920px !important; height: 1080px !important; overflow: hidden !important; box-sizing: border-box !important; position: relative; isolation: isolate }
aside { display: none !important }
h1 { font-size: 96px; font-weight: 600 } h2 { font-size: 64px; font-weight: 600 } h3 { font-size: 44px; font-weight: 600 }
p, li, h1, h2, h3 { overflow-wrap: break-word; text-wrap: pretty }
body > section > img:first-child, body > section > svg:first-child { z-index: -1 }
.win, .win-vec, .tangent, .bleed-r, .case-ph-r, .case-ph-l, .venn, .ring, .vec, .tex-band, .window-left, .window-vec, .wire, .rings, .g-host, .backdrop { z-index: -1 }
.tex-band { z-index: -2 !important }
"""
faces = "".join(
    f"@font-face {{ font-family: '{f['family']}'; src: url({fix(f['src'])}); font-weight: 100 900; }}\n"
    for f in deck["faces"].values() if "src" in f
)
css = fix(open(os.path.join(root, "project", "deck.css"), encoding="utf-8").read())
slides = "\n".join(
    fix(open(os.path.join(root, "project", "slides", sid + ".html"), encoding="utf-8").read())
    for sid in deck["order"] if os.path.exists(os.path.join(root, "project", "slides", sid + ".html"))
)
html = f"<!doctype html><html><head><meta charset='utf-8'><style>{base}{faces}{css}</style></head><body>{slides}</body></html>"
open(os.path.join(outdir, "index.html"), "w", encoding="utf-8").write(html)
print(len(deck["order"]))
