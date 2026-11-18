import re, os, math
os.chdir(r"C:/Users/luiz_/AppData/Local/Temp/claude/fc8a705dbf4edc7e/a63ed5d7-099b-46ea-b146-a5c5ac858cae/scratchpad/realm-v14/project")
def rd(p): return open(p, encoding='utf-8').read()
def wr(p, s): open(p, 'w', encoding='utf-8').write(s)
def sub1(s, a, b):
    assert a in s, a[:70]
    return s.replace(a, b)

STORY = '/_blob/f97ca29bf64a043d2b795179af7b8f5e'
WATER = '/_blob/fe345eab28eba8d6241361f8e7c47f1a'
CYP = '/_blob/958efb4f25f7869d4d836a3810b8f46b'
GLASS = '/_blob/f5c05c6d7dbb6ecb0c90d946325c56fb'
OLIVE = '/_blob/ede2b641055cc5c3aa598c1b48c9c9c7'
COLON = '/_blob/64fbdec2785d821d45d509b9550d5677'

# ---------------- CSS ----------------
css = rd('deck.css')
css = sub1(css, ".beat-tick { width: 3px; height: 26px; background: var(--slate); margin-top: -40px; margin-bottom: 12px; }",
           ".beat-tick { width: 14px; height: 14px; border-radius: 7px; background: var(--slate); margin-top: -33px; margin-bottom: 12px; }")
css = sub1(css, "/* photo windows (v2.1): one whole photograph in a box, Paper arcs crossing it as a vector layer; no text on top */",
           "/* photo windows: one whole photograph in a box, no pattern on top, no text on top */")
if '.item-h' not in css:
    css += '''
/* drawn vectors (as in the v1.3 native file): ring-segment glyphs, segmented rings, location pins, quadrant icons */
.item-h { display: flex; align-items: center; gap: 18px; }
.glyph { width: 56px; height: 56px; flex: 0 0 auto; }
.glyph.s { width: 40px; height: 40px; }
.loc { display: flex; align-items: center; gap: 12px; }
.pin { width: 22px; height: 28px; flex: 0 0 auto; }
.q-icon { width: 44px; height: 44px; color: var(--slate); }
.hub-core.drawn { background: none; position: relative; padding: 0; }
.hub-label { position: absolute; left: 60px; top: 160px; width: 280px; text-align: center; }
.seg-n { position: absolute; width: 52px; font-size: 24px; line-height: 52px; text-align: center; margin: 0; font-variant-numeric: tabular-nums; }
'''
wr('deck.css', css)

def arc_path(cx, cy, r, a1, a2):
    x1 = cx + r * math.cos(math.radians(a1)); y1 = cy + r * math.sin(math.radians(a1))
    x2 = cx + r * math.cos(math.radians(a2)); y2 = cy + r * math.sin(math.radians(a2))
    large = 1 if (a2 - a1) % 360 > 180 else 0
    return f'M{x1:.1f} {y1:.1f}A{r} {r} 0 {large} 1 {x2:.1f} {y2:.1f}'

def glyph(k, n, cls='glyph'):
    # ring-segment glyph: a Stone ring with k of n segments in Slate
    segs = ''
    for i in range(n):
        a1 = -90 + 360 * i / n + 6; a2 = -90 + 360 * (i + 1) / n - 6
        col = '#8693A6' if i < k else '#D9D4CC'
        segs += f'<path d="{arc_path(28, 28, 22, a1, a2)}" stroke="{col}"/>'
    return (f'<svg class="{cls}" aria-label="Ring with {k} of {n} segments filled" viewBox="0 0 56 56" width="56" height="56" '
            f'xmlns="http://www.w3.org/2000/svg"><g fill="none" stroke-width="7" stroke-linecap="butt">{segs}</g></svg>')

PIN = ('<svg class="pin" aria-label="Location" viewBox="0 0 22 28" width="22" height="28" xmlns="http://www.w3.org/2000/svg">'
       '<path d="M11 0C4.9 0 0 4.8 0 10.8C0 18.9 11 28 11 28S22 18.9 22 10.8C22 4.8 17.1 0 11 0Z" fill="#8693A6"/>'
       '<circle cx="11" cy="10.8" r="4" fill="#F6F3EE"/></svg>')

def rings_bg(left, top, w, h, cx, cy, rmin, rmax, step):
    circ = ''.join(f'<circle cx="{cx}" cy="{cy}" r="{r}"/>' for r in range(rmin, rmax + 1, step))
    return (f'<svg class="win-vec" aria-label="Concentric REALM rings" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'style="left:{left}px;top:{top}px" xmlns="http://www.w3.org/2000/svg"><g fill="none" stroke="#DCD6CC" stroke-width="1.5">{circ}</g></svg>\n')

def set_aside(s, text):
    return re.sub(r'<aside>.*?</aside>', lambda m: f'<aside>{text}</aside>', s, flags=re.S)

# ---------------- overview: photo + 2x2 pillars ----------------
s = rd('slides/overview.html')
s = re.sub(r'<div class="spacer"></div>\n<div class="cols c4">.*?</div>\n</div>\n<div class="foot">', lambda m: (
    '<div class="spacer"></div>\n<div class="g12" style="align-items:end">\n'
    f'<img src="{GLASS}" alt="A glass facade reflecting a classical limestone building against a clear sky" style="grid-column:1 / 5;width:560px;height:560px;object-fit:cover">\n'
    '<div class="quad" style="grid-column:5 / 13">\n'
    '<div class="q"><h3 class="h28">Families</h3><p class="body">The nation’s most successful families, investing through single-family offices, multi-family offices, and directly as principals.</p></div>\n'
    '<div class="q"><h3 class="h28">How REALM serves</h3><p class="body">REALM gives each family Access, Advice, and Actionable Intel: proprietary opportunities, guidance on the family’s real estate, and ground-level market insight.</p></div>\n'
    '<div class="q"><h3 class="h28">Strategies</h3><p class="body">Strategies across the risk-return spectrum and the capital stack, from durable, tax-efficient income to complex, distressed, and forced-sale opportunities, with credit, GP, and secondaries to follow.</p></div>\n'
    '<div class="q"><h3 class="h28">Process</h3><p class="body">Each relationship follows five steps: understand the family, construct its allocation, select through the REALM Factor Framework, manage through the full lifecycle, and share what REALM learns.</p></div>\n'
    '</div>\n</div>\n<div class="foot">'), s, flags=re.S)
s = set_aside(s, 'v1.3 slide 4. The subtitle becomes the title (the module cover already says “Firm Overview”). New layout: a photograph (glass reflecting stone) beside the four pillars in a 2 × 2 grid, which closes the empty band the four thin columns left. Copy lightly trimmed for length: “How REALM serves” drops “investment” and “drawn from REALM’s investments, operating partners, and families”; “Strategies” drops “throughout” and “strategies”; “Process” is the short form (page 26 tells it in full). REALM to approve. The KPIs live on Proof (page 34).')
wr('slides/overview.html', s)

# ---------------- story: new photo, no arcs ----------------
s = rd('slides/story.html')
s = re.sub(r'<img class="win"[^>]*>\n<svg class="win-vec".*?</svg>\n', lambda m:
           f'<img class="win" src="{STORY}" alt="Limestone building with arched windows and olive trees against a clear sky" style="left:976px;top:0;width:944px;height:500px">\n', s, flags=re.S)
s = s.replace('Photo window from v2.1 (cypress) top right; text stays on Paper.', 'Photograph (limestone and olive trees, Magnific Cinematic) top right, no pattern on it; text stays on Paper. Milestones marked with Slate dots, as in the v1.3 timeline.')
wr('slides/story.html', s)

# ---------------- opportunity: new water, no arcs ----------------
s = rd('slides/opportunity.html')
s = re.sub(r'<img class="win"[^>]*>\n<svg class="win-vec".*?</svg>\n', lambda m:
           f'<img class="win" src="{WATER}" alt="Concentric ripples on clear, shallow water over a pale stone floor" style="left:976px;top:0;width:944px;height:440px">\n', s, flags=re.S)
s = s.replace('Photo window from v2.1 (water) with Paper arcs crossing it; no text sits on the image.', 'Photograph (water ripples, Magnific Cinematic), no pattern on it; no text sits on the image.')
wr('slides/opportunity.html', s)

# ---------------- capital-four: new cypress, no arcs, icons ----------------
s = rd('slides/capital-four.html')
s = re.sub(r'<img class="win"[^>]*>\n<svg class="win-vec".*?</svg>\n', lambda m:
           f'<img class="win" src="{CYP}" alt="A row of cypress trees against a clear sky" style="left:0;top:470px;width:648px;height:490px">\n', s, flags=re.S)
for name, icon in [('Values', 'Trust'), ('Knowledge', 'Lightbulb'), ('Resources', 'Chart'), ('Relationships', 'Users')]:
    s = s.replace(f'<div class="q"><h3 class="h48">{name}</h3>', f'<div class="q"><x-icon name="{icon}" class="q-icon"></x-icon><h3 class="h48">{name}</h3>')
s = set_aside(s, 'v1.3 slide 8 without the repeated quote. Four quadrants, each with an icon as in the v1.3 native file. Photograph (cypress, Magnific Cinematic) under the left column, no pattern on it. The lede on the left is new connective copy (REALM to approve or drop).')
wr('slides/capital-four.html', s)

# ---------------- why now B: photo in the fourth column ----------------
s = rd('slides/whynow-b.html')
s = sub1(s, '<div class="mx m3">\n<div></div>\n', '<div class="mx">\n<div></div>\n'
         f'<img src="{OLIVE}" alt="An olive tree beside a limestone wall against a clear sky" style="grid-column:5;grid-row:1 / 4;width:347px;height:470px;object-fit:cover;align-self:start">\n')
s = set_aside(s, 'v1.3 slide 7, drivers 05 to 07. Same matrix and column widths as the previous slide; the fourth column carries a photograph (olive tree and limestone, Magnific Cinematic) instead of standing empty. Driver 07 refers to current tax law: compliance to confirm the wording.')
wr('slides/whynow-b.html', s)

# ---------------- lifecycle: colonnade photo right ----------------
s = rd('slides/lifecycle.html')
s = re.sub(r'<section id="lifecycle">\n<div class="band">\n<h2 class="title">Lifecycle Management</h2>\n<p class="lede">(.*?)</p>\n</div>\n<p class="h48" style="width:1428px;margin-top:72px">',
           lambda m: ('<section id="lifecycle">\n'
                      f'<img class="win" src="{COLON}" alt="A travertine colonnade against a clear sky" style="left:1124px;top:0;width:796px;height:600px">\n'
                      '<div class="stack" style="width:1004px;gap:24px">\n<h2 class="title">Lifecycle Management</h2>\n'
                      f'<p class="lede">{m.group(1)}</p>\n</div>\n<p class="h48" style="width:1004px;margin-top:56px">'), s, flags=re.S)
s = set_aside(s, 'v1.3 slide 16: the accountability statement large, then three stages in sequence. Photograph (travertine colonnade, Magnific Cinematic) top right. Copy unchanged.')
wr('slides/lifecycle.html', s)

# ---------------- formula: ring-segment glyphs ----------------
s = rd('slides/formula.html')
for i, n in enumerate(['Access', 'Advice', 'Actionable Intel'], 1):
    s = sub1(s, f'<div class="item"><p class="h48">{n}</p>', f'<div class="item"><div class="item-h">{glyph(i, 3)}<p class="h48">{n}</p></div>')
for i, n in enumerate(['Alignment', 'Acumen', 'Agility', 'Attentiveness'], 1):
    s = sub1(s, f'<div class="item"><p class="h28">{n}</p>', f'<div class="item"><div class="item-h">{glyph(i, 4, "glyph s")}<p class="h28">{n}</p></div>')
s = set_aside(s, 'v1.3 slide 10, first half: the three things families receive (larger, on the left) and the four ways REALM delivers them. Each item carries a ring-segment glyph drawn from the REALM rings, one segment per item, so the three and the four read as complete sets. The Three Cs move to their own slide. Copy unchanged.')
wr('slides/formula.html', s)

# ---------------- what REALM does: segmented ring ----------------
s = rd('slides/does.html')
cols = ['#DCE1E8', '#B7C0CD', '#8693A6', '#55627A', '#1D2430']
txt = ['#1D2430', '#1D2430', '#1D2430', '#F6F3EE', '#F6F3EE']
segs = ''.join(f'<path d="{arc_path(276, 276, 230, -90 + 72 * k + 2, -90 + 72 * (k + 1) - 2)}" stroke="{cols[k]}"/>' for k in range(5))
ring = (f'<svg class="ring" aria-label="A ring of five segments, one per service, around the family at its centre" viewBox="0 0 552 552" width="552" height="552" xmlns="http://www.w3.org/2000/svg">'
        f'<g fill="none" stroke-width="56">{segs}</g><circle cx="276" cy="276" r="150" fill="#ECE7E0"/></svg>')
s = re.sub(r'<svg class="ring".*?</svg>', lambda m: ring, s, flags=re.S)
s = re.sub(r'<p class="ring-n"[^>]*>\d</p>\n', '', s)
labels = ''
for k in range(5):
    a = math.radians(-54 + 72 * k)
    x = 960 + 230 * math.cos(a); y = 530 + 230 * math.sin(a)
    labels += f'<p class="seg-n" style="left:{x - 26:.0f}px;top:{y - 26:.0f}px;color:{txt[k]}">{k + 1}</p>\n'
s = sub1(s, '<p class="ring-c">The family</p>', labels + '<p class="ring-c">The family</p>')
s = set_aside(s, 'v1.3 slide 11: the five services as segments of one ring around the family, drawn like the ring-segment diagram in the v1.3 native file, light to dark in order. The numbered list on the right is the index for the next five slides. Copy unchanged.')
wr('slides/does.html', s)

# ---------------- intel: drawn hub ----------------
s = rd('slides/intel.html')
quad = ''.join(f'<path d="{arc_path(200, 200, 186, a + 10, a + 80)}"/>' for a in (-90, 0, 90, 180))
hub = ('<div class="hub-core drawn"><svg aria-label="A centre circle inside four ring segments, one toward each channel" viewBox="0 0 400 400" width="400" height="400" xmlns="http://www.w3.org/2000/svg">'
       f'<g fill="none" stroke="#B7C0CD" stroke-width="16">{quad}</g><circle cx="200" cy="200" r="150" fill="#DCE1E8"/></svg>'
       '<p class="h28 hub-label">Insight and the REALM network</p></div>')
s = re.sub(r'<div class="hub-core">.*?</div>', lambda m: hub, s, flags=re.S)
wr('slides/intel.html', s)

# ---------------- works: light trims ----------------
s = rd('slides/works.html')
trims = [
 ('The relationship usually starts with an introduction from another family. REALM then learns the family’s portfolio, tax position, holding-period objectives, and goals for the next generation, and that understanding becomes the brief for every recommendation that follows.',
  'The relationship usually starts with an introduction from another family. REALM learns the family’s portfolio, tax position, holding-period objectives, and goals for the next generation: the brief for every recommendation.'),
 ('REALM and the family build the strategy together: the role real estate plays in the portfolio, the strategies that fit, and the structures that suit the family’s tax position. The strategy serves as the foundation for every investment that follows.',
  'REALM and the family build the strategy together: the role real estate plays in the portfolio, the strategies that fit, and the structures that suit the family’s tax position.'),
 ('Opportunities come off-market from operating partners, brokers, and the families themselves, and pass through the REALM Factor Framework and asset-level diligence. Opportunities that clear both proceed with an asset-level business plan.',
  'Opportunities come off-market from operating partners, brokers, and the families themselves, and pass through the REALM Factor Framework and asset-level diligence before a business plan is set.'),
 ('What REALM learns from its investments, partners, and families returns to its families through roundtables, webinars, and white papers, and informs the next allocation and the next introduction.',
  'What REALM learns from its investments, partners, and families returns to its families through roundtables, webinars, and white papers, and informs the next allocation.'),
]
for a, b in trims: s = sub1(s, a, b)
s = set_aside(s, 'v1.3 slide 17: five steps, each a shade darker, so the eye reads them as one progression. Copy lightly trimmed for length (steps 1, 2, 3 and 5 lose a closing clause; meaning unchanged). REALM to approve.')
wr('slides/works.html', s)

# ---------------- advantage: light trims ----------------
s = rd('slides/advantage.html')
s = sub1(s, ' and the generations that follow, and each family invests alongside families who share its priorities.', ' and the generations that follow.')
s = sub1(s, ' The REALM Factor Framework turns that insight into a read on each dislocation, and REALM looks for quality real estate trading below intrinsic value.', ' The REALM Factor Framework turns that insight into a read on each dislocation.')
s = re.sub(r'(<aside>.*?)(</aside>)', lambda m: m.group(1) + ' Cards 1 and 4 lightly trimmed for length (closing clauses); REALM to approve.' + m.group(2), s, flags=re.S)
wr('slides/advantage.html', s)

# ---------------- cases: location pins ----------------
for f in ['case-cityspire', 'case-willow', 'case-mh', 'case-land', 'case-boston', 'case-sanjose', 'case-family']:
    s = rd(f'slides/{f}.html')
    if 'class="loc"' not in s:
        s = re.sub(r'(</h2>\n)<p class="lede">(.*?)</p>', lambda m: f'{m.group(1)}<div class="loc">{PIN}<p class="lede">{m.group(2)}</p></div>', s, count=1)
    wr(f'slides/{f}.html', s)

# ---------------- contents and disclaimer: concentric rings from the Bold+ moodboard ----------------
s = rd('slides/contents.html')
if 'win-vec' not in s:
    s = s.replace('<section id="contents">\n', '<section id="contents">\n' + rings_bg(0, 380, 900, 700, 330, 700, 90, 570, 60))
wr('slides/contents.html', s)
s = rd('slides/disclaimer.html')
if 'win-vec' not in s:
    s = s.replace('<section id="disclaimer">\n', '<section id="disclaimer">\n' + rings_bg(0, 260, 680, 820, 160, 820, 90, 630, 60))
wr('slides/disclaimer.html', s)
print('ok')
