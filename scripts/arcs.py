"""Build REALM Bold arc assets: oversized concentric bands, some filled with painted texture."""
import sys, os
from PIL import Image, ImageDraw, ImageEnhance

img_dir = sys.argv[1]
out = sys.argv[2]
os.makedirs(out, exist_ok=True)
S = 3  # supersample

# strokes run along the bands (vertical in the visible part of the rings), a touch more colour
texture = Image.open(os.path.join(img_dir, "texture.png")).convert("RGB").rotate(90, expand=True)
texture = ImageEnhance.Color(texture).enhance(1.35)


def ring_mask(size, cx, cy, r_out, width):
    W, H = size
    m = Image.new("L", (W * S, H * S), 0)
    d = ImageDraw.Draw(m)
    d.ellipse([(cx - r_out) * S, (cy - r_out) * S, (cx + r_out) * S, (cy + r_out) * S], fill=255)
    r_in = r_out - width
    d.ellipse([(cx - r_in) * S, (cy - r_in) * S, (cx + r_in) * S, (cy + r_in) * S], fill=0)
    return m.resize((W, H), Image.LANCZOS)


def fill_layer(size, fill):
    if fill == "texture":
        W, H = size
        k = max(W / texture.width, H / texture.height)
        t = texture.resize((round(texture.width * k), round(texture.height * k)), Image.LANCZOS)
        l, tp = (t.width - W) // 2, (t.height - H) // 2
        return t.crop((l, tp, l + W, tp + H)).convert("RGBA")
    return Image.new("RGBA", size, fill)


def arcs(size, cx, cy, bands, base=None, bg=None):
    # opaque ground + alpha_composite: anti-aliased edges blend into the real ground colour,
    # never into transparent black (which left dark hairlines along every band)
    if base is not None:
        canvas = base.convert("RGBA")
    else:
        canvas = Image.new("RGBA", size, bg or (0, 0, 0, 0))
    for r_out, width, fill in bands:
        layer = fill_layer(size, fill).copy()
        layer.putalpha(ring_mask(size, cx, cy, r_out, width))
        canvas = Image.alpha_composite(canvas, layer)
    return canvas


FULL = (1920, 1080)
CX, CY = 2500, 430

light_bands = [
    (1810, 18, "#E7E4DD"),
    (1610, 54, "#DCDAD2"),
    (1350, 114, "#D5D4CB"),
    (1160, 46, "texture"),
    (955, 86, "texture"),
]
dark_bands = [
    (1810, 18, "#212935"),
    (1610, 54, "#232C38"),
    (1350, 114, "#252E3B"),
    (1160, 46, "texture"),
    (955, 86, "texture"),
]
arcs(FULL, CX, CY, light_bands, bg="#F6F3EE").convert("RGB").save(os.path.join(out, "arcs-light.png"))
arcs(FULL, CX, CY, dark_bands, bg="#1D2430").convert("RGB").save(os.path.join(out, "arcs-dark.png"))
# quiet version for content slides: tone-on-tone only, no texture
quiet_bands = [
    (1810, 18, "#212935"),
    (1610, 54, "#232C38"),
    (1350, 114, "#252E3B"),
    (1160, 46, "#232C38"),
    (955, 86, "#212935"),
]
arcs(FULL, CX, CY, quiet_bands, bg="#1D2430").convert("RGB").save(os.path.join(out, "arcs-dark-quiet.png"))

# arcs as windows: water photo with Paper bands rising from below
water = Image.open(os.path.join(img_dir, "gap-water.png")).convert("RGB")
pw, ph = 860, 1080
scale = max(pw / water.width, ph / water.height)
w2 = water.resize((round(water.width * scale), round(water.height * scale)), Image.LANCZOS)
left = (w2.width - pw) // 2
top = (w2.height - ph) // 2
panel = w2.crop((left, top, left + pw, top + ph))
paper_bands = [(980, 40, "#F6F3EE"), (830, 48, "#F6F3EE"), (670, 60, "#F6F3EE")]
arcs((pw, ph), 300, 1560, paper_bands, base=panel).convert("RGB").save(os.path.join(out, "gap-window.jpg"), quality=90)

# cypress, vertical crop for the markets slide (sky left, trees right)
cyp = Image.open(os.path.join(img_dir, "divider-cypress.png")).convert("RGB")
crop_w = round(cyp.height * 600 / 792)
x0 = 1150
cyp = ImageEnhance.Color(cyp).enhance(0.82)
cyp.crop((x0, 0, x0 + crop_w, cyp.height)).save(os.path.join(out, "where-cypress.jpg"), quality=90)
print("ok")
