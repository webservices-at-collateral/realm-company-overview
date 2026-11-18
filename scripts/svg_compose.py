"""Compose 1920x1080 SVG backdrops from the REALM ring assets (vector), with the painted
texture clipped into the thickest crescent where asked."""
import sys, os, re, base64, io
from PIL import Image

asset1, asset2, texture_path, out = sys.argv[1:5]
os.makedirs(out, exist_ok=True)


def paths(svg_path):
    t = open(svg_path, encoding="utf-8").read()
    return re.findall(r'<path[^>]*\sd="([^"]+)"', t)


def thickness_order(ds):
    # crude: longer path data ~ same; use bbox width from numbers to find the innermost (smallest) ring
    def bbox(d):
        nums = list(map(float, re.findall(r"-?\d+\.?\d*", d)))
        xs, ys = nums[0::2], nums[1::2]
        return max(xs) - min(xs)
    return sorted(range(len(ds)), key=lambda i: bbox(ds[i]))  # smallest first


tex = Image.open(texture_path).convert("RGB").rotate(90, expand=True)
tex.thumbnail((1400, 1400))
buf = io.BytesIO(); tex.save(buf, "JPEG", quality=78)
tex_b64 = base64.b64encode(buf.getvalue()).decode()


def compose(name, src, size, scale, center, fills, opacity=1.0, texture_inner=False):
    ds = paths(src)
    order = thickness_order(ds)  # order[0] = innermost
    W, H = size
    sx, sy = src_size[src]
    cx, cy = center
    tx = cx - scale * sx / 2
    ty = cy - scale * sy / 2
    defs = ""
    if texture_inner:
        defs = (f'<defs><pattern id="tex" patternUnits="userSpaceOnUse" x="0" y="0" width="{sx}" height="{sy}">'
                f'<image href="data:image/jpeg;base64,{tex_b64}" x="0" y="0" width="{sx}" height="{sy}" preserveAspectRatio="xMidYMid slice"/>'
                f'</pattern></defs>')
    body = []
    for i, d in enumerate(ds):
        inner = (i == order[0])
        if inner and texture_inner:
            body.append(f'<path d="{d}" fill="url(#tex)"/>')
        else:
            body.append(f'<path d="{d}" fill="{fills}" opacity="{opacity}"/>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{defs}'
           f'<g transform="translate({tx:.1f} {ty:.1f}) scale({scale})">{"".join(body)}</g></svg>')
    open(os.path.join(out, name), "w", encoding="utf-8").write(svg)
    print(name, len(svg))


src_size = {asset1: (2169, 2183), asset2: (2968, 2974)}
# cover: light ground, rings cropped by the right edge, thickest crescent opens onto paint
compose("cover-rings.svg", asset1, (1920, 1080), 0.78, (1780, 560), "#C9C5BF", 1.0, texture_inner=True)
# close: dark ground, tone-on-tone rings, thickest crescent in paint
compose("close-rings.svg", asset2, (1920, 1080), 0.62, (1720, 560), "#B5B1AB", 0.19, texture_inner=True)
# quiet light rings for a content slide (no texture)
compose("quiet-rings.svg", asset1, (1920, 1080), 0.45, (1820, 150), "#E2DED7", 1.0)
