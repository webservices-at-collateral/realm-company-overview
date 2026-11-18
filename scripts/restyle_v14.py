import re, os
os.chdir(r"C:/Users/luiz_/AppData/Local/Temp/claude/fc8a705dbf4edc7e/a63ed5d7-099b-46ea-b146-a5c5ac858cae/scratchpad/realm-v14/project")
def rd(p): return open(p, encoding='utf-8').read()
def wr(p, s): open(p, 'w', encoding='utf-8').write(s)

QUIET = '<img class="vec" src="/_blob/e1f0f2c68725ff735f8d42a375402d78" alt="">\n'
WATER = '/_blob/d5122d2ca66f1448980d92820b301987'
CYP = '/_blob/b9abb2803c8678aa983dc2de2facbfec'
CYPT = '/_blob/dc296ed6a62a344598badfe2d182dce5'

# ---------- CSS ----------
css = rd('deck.css')
old = ".mod-right { grid-column: 9 / 13; display: flex; flex-direction: column; justify-content: flex-end; }"
assert old in css
css = css.replace(old, ".mod-right { grid-column: 9 / 13; align-self: end; display: flex; flex-direction: column; background: var(--harbor); margin: 0 -32px; padding: 20px 32px; }  /* Harbor panel: the list never sits on the wireframe */")
if '.dt {' not in css:
    css += '''
/* photo windows (v2.1): one whole photograph in a box, Paper arcs crossing it as a vector layer; no text on top */
.win { position: absolute; object-fit: cover; }
.win-vec { position: absolute; }

/* data tables as div grids (Slides keeps every style here): Harbor header, Sentient first column,
   REALM's answer always on a light Slate band, so the REALM side reads the same on every comparison */
.dt { display: flex; flex-direction: column; width: 1744px; }
.dt-row { display: grid; column-gap: 32px; border-bottom: 1px solid var(--line); align-items: stretch; }
.dt-row.head { background: var(--harbor); border-bottom: none; }
.dt-row.z { background: var(--bg2); }
.cmp { grid-template-columns: 330px 520px 1fr; padding-left: 24px; }
.cmp-d { grid-template-columns: 360px 540px 1fr; padding-left: 24px; }
.strat { grid-template-columns: 300px 500px 250px 210px 1fr; padding: 0 24px; }
.dt-c { padding: 18px 0 20px; }
.dt-hl { padding: 18px 24px 20px; background: var(--slate-tint); }
.head .dt-c, .head .dt-hl { padding-top: 14px; padding-bottom: 14px; }
.head .dt-hl { background: var(--slate); }
.dt-h { font-size: 24px; line-height: 1.3; font-weight: 600; color: var(--paper); margin: 0; }
.dt-h.on-slate { color: var(--harbor); }
.dt-k { font-family: 'Sentient', Georgia, serif; font-weight: 400; font-size: 28px; line-height: 1.18; color: var(--harbor); margin: 0; }
.dt-t { font-size: 24px; line-height: 1.35; color: var(--body); margin: 0; }
.dt-t.ink { color: var(--harbor); }
.dt-t.live { color: var(--harbor); font-weight: 600; }
'''
wr('deck.css', css)

# ---------- comparison tables ----------
def cmp_table(cls, heads, rows):
    h = (f'<div class="dt-row head {cls}"><div class="dt-c"><p class="dt-h">{heads[0]}</p></div>'
         f'<div class="dt-c"><p class="dt-h">{heads[1]}</p></div>'
         f'<div class="dt-hl"><p class="dt-h on-slate">{heads[2]}</p></div></div>')
    b = ''.join(f'\n<div class="dt-row {cls}"><div class="dt-c"><p class="dt-k">{k}</p></div>'
                f'<div class="dt-c"><p class="dt-t">{a}</p></div>'
                f'<div class="dt-hl"><p class="dt-t ink">{c}</p></div></div>' for k, a, c in rows)
    return f'<div class="dt">\n{h}{b}\n</div>'

def swap_table(f, newtable, drop_quiet=False, lede_w=None):
    s = rd(f)
    s = re.sub(r'<table class="t">.*?</table>', lambda m: newtable, s, flags=re.S)
    if drop_quiet:
        s = s.replace(QUIET, '')
    if lede_w:
        s = s.replace('style="width:1282px;margin-top:20px"', f'style="width:{lede_w}px;margin-top:20px"')
    wr(f, s)

fundA = [('Alignment', 'Minimal investment from principals', 'Paid mainly on performance, after families receive their preferred return and their capital back'),
         ('Control', 'Commingled fund structure', 'Families choose deal by deal through REALM Direct, or decline deals inside the series vehicle'),
         ('Fees', 'Full fees and a double promote', 'Lower fees and no double promote'),
         ('Liquidity', 'Locked up for the life of the fund', 'Investments chosen one at a time, with an evergreen income strategy in development'),
         ('Opportunity assessment', 'Backward-looking and data-driven', 'Forward-looking: the REALM Factor Framework reads dislocation and trends'),
         ('Diversification', 'Narrowly targeted by property type and geography', 'Broad, across property types and geographies'),
         ('Personal relationship', 'None', 'Direct access to the team')]
fundB = [('Tax', 'Built largely for tax-exempt investors', 'Built around each family’s tax position'),
         ('Target deals', 'Large checks set by fund size and the fee model', 'Middle-market transactions that large funds overlook'),
         ('Advice', 'Not offered', 'Real estate allocation advice, portfolio reviews, and a second opinion on opportunities families bring in'),
         ('1031 exchanges', 'Not offered', 'Yes, through tenancy-in-common interests in REALM investments'),
         ('Intelligence', 'Not shared', 'The ground-level read of REALM’s families and operating partners, shared back with them'),
         ('Transparency', 'Limited', 'Each asset reported against its original underwriting, good news and bad')]
swap_table('slides/fund-a.html', cmp_table('cmp', ['Criterion', 'The Fund Model', 'REALM'], fundA), drop_quiet=True)
swap_table('slides/fund-b.html', cmp_table('cmp', ['Criterion', 'The Fund Model', 'REALM'], fundB), drop_quiet=True)

difA = [('A patient, long-term horizon', 'Families invest for the generations that follow, well beyond any single hold period.', 'Hold periods shaped by each family’s objectives and each investment’s business plan.'),
        ('Preservation before growth', 'Families protect what they have built before they reach for income and growth.', 'Underwriting through the REALM Factor Framework and asset-level diligence before each commitment.'),
        ('Tax sensitivity', 'Families measure every return after tax, across trusts, entities, and generations.', 'Direct ownership, with depreciation, cost segregation, and 1031 exchanges structured around the family’s tax position.'),
        ('Control', 'Families want a say in what they own and how their capital is put to work.', 'Strategies across the risk-return spectrum, with each family choosing its strategies and its level of participation.')]
difB = [('Transparency and clear reporting', 'Families expect to see how their capital is performing, in plain terms.', 'Clear, consistent reporting on each investment, with candid updates when plans change.'),
        ('Relationships first', 'Families invest with people they know, often on the word of a family they respect.', 'Direct access to REALM’s team, and a network of families built largely through introductions.'),
        ('Legacy beyond money', 'Families judge success by what passes to the next generation, in values as well as capital.', 'A place for the next generation in the family’s real estate decisions, and gatherings that bring generations together.'),
        ('Liquidity that matters', 'Families want to know when and how their capital returns.', 'Investments chosen with each family’s liquidity needs in view, and exits timed to the market.'),
        ('Customization', 'Every family’s holdings, tax position, and goals are its own.', 'A real estate allocation constructed with each family from strategies across the risk-return spectrum.')]
swap_table('slides/different-a.html', cmp_table('cmp-d', ['Priority', 'For a family', 'How REALM answers'], difA), lede_w=1004)
swap_table('slides/different-b.html', cmp_table('cmp-d', ['Priority', 'For a family', 'How REALM answers'], difB), lede_w=1004)

# ---------- strategies table ----------
strat = [('Tactical Opportunities', 'Complex, distressed, and forced-sale situations', 'Series vehicle, up to 5 years', 'High', 'Live'),
         ('Diversified Income', 'Durable, tax-efficient income from direct, net-lease, and off-market acquisitions', 'Evergreen, 10+ years', 'Low', 'In development, targeted for early 2027'),
         ('Tax-Deferred Exchange', 'Homes for 1031 and 721 exchange capital', 'To be set', 'Low', '1031 live through tenancy-in-common interests; 721 planned'),
         ('Opportunistic Credit', 'Distressed and non-performing loans, whole or structured', 'Up to 3 years', 'High to moderate', 'Planned, 2027, market permitting'),
         ('Structured Credit', 'Bespoke senior and subordinated loan origination', 'Up to 3 years', 'Moderate to low', 'Planned'),
         ('GP Opportunities', 'Programmatic co-GP positions and GP stakes', 'Up to 7 years', 'Moderate to high', 'Planned'),
         ('Secondaries', 'Interests in existing real estate partnerships', 'Up to 7 years', 'Moderate', 'Planned')]
h = '<div class="dt-row head strat">' + ''.join(f'<div class="dt-c"><p class="dt-h">{x}</p></div>' for x in ['Strategy', 'Target', 'Structure and hold', 'Risk', 'Status']) + '</div>'
rows = ''
for i, (a, b, c, d, e) in enumerate(strat):
    z = ' z' if i % 2 == 0 else ''
    ecls = 'dt-t live' if e == 'Live' else 'dt-t'
    rows += (f'\n<div class="dt-row strat{z}"><div class="dt-c"><p class="dt-k">{a}</p></div><div class="dt-c"><p class="dt-t">{b}</p></div>'
             f'<div class="dt-c"><p class="dt-t">{c}</p></div><div class="dt-c"><p class="dt-t">{d}</p></div><div class="dt-c"><p class="{ecls}">{e}</p></div></div>')
swap_table('slides/access.html', f'<div class="dt">\n{h}{rows}\n</div>')

# ---------- advantage: rings ran behind the cards ----------
s = rd('slides/advantage.html'); wr('slides/advantage.html', s.replace(QUIET, ''))

# ---------- capital-def: definition moved left, clear of the arcs ----------
s = rd('slides/capital-def.html')
s = re.sub(r'<svg class="vec".*?</svg>', lambda m: '<svg class="vec" aria-label="Oversized REALM arcs cut by the right edge, one step lighter than Slate" viewBox="0 0 1920 1080" width="1920" height="1080" xmlns="http://www.w3.org/2000/svg"><g fill="none"><circle cx="2500" cy="430" r="1293" stroke="#95A1B2" stroke-width="114"/><circle cx="2500" cy="430" r="1137" stroke="#7D8A9D" stroke-width="46"/><circle cx="2500" cy="430" r="912" stroke="#7D8A9D" stroke-width="86"/></g></svg>', s, flags=re.S)
s = s.replace('<div class="def-text" style="grid-row:2">', '<div class="def-text" style="grid-row:2;grid-column:1 / 8">')
wr('slides/capital-def.html', s)

def arcs(w, h, cx, cy, rs, ws, left, top):
    circ = ''.join(f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke-width="{sw}"/>' for r, sw in zip(rs, ws))
    return (f'<svg class="win-vec" aria-label="Three Paper arcs crossing the photograph" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'style="left:{left}px;top:{top}px" xmlns="http://www.w3.org/2000/svg"><g fill="none" stroke="#F6F3EE">{circ}</g></svg>\n')

# ---------- opportunity: v1.3's own opening line as headline, water window top right ----------
s = rd('slides/opportunity.html')
win = (f'<img class="win" src="{WATER}" alt="Concentric ripples on clear, shallow water over a pale stone floor" style="left:976px;top:0;width:944px;height:440px">\n'
       + arcs(944, 440, 300, 900, [820, 690, 560], [34, 44, 56], 976, 0))
s = s.replace(QUIET, win)
s = s.replace('<h2 class="title">The Opportunity</h2>', '<h2 class="title" style="width:856px">Families invest with priorities of their own.</h2>')
s = s.replace('<p class="lede">Families invest with priorities of their own:</p>', '<p class="lede">What families value:</p>')
s = re.sub(r'<aside>.*?</aside>', lambda m: '<aside>v1.3 slide 5 (“The Opportunity”). Headline: v1.3’s own opening line, so no new slogan; the left column label becomes “What families value”. Read as an argument in three parts: what families want, why conventional structures leave it unserved (Harbor panel), and what REALM offers. Photo window from v2.1 (water) with Paper arcs crossing it; no text sits on the image.</aside>', s, flags=re.S)
wr('slides/opportunity.html', s)

# ---------- story: headline from v1.3, cypress window top right ----------
s = rd('slides/story.html')
win = (f'<img class="win" src="{CYP}" alt="A row of cypress trees against a clear sky" style="left:976px;top:0;width:944px;height:500px">\n'
       + arcs(944, 500, 300, 980, [820, 690, 560], [34, 44, 56], 976, 0))
s = s.replace(QUIET, win)
s = s.replace('<div class="band">\n<h2 class="title">The Founding Story</h2>\n<p class="lede">REALM began with a conviction: Family Capital deserves real estate investment built intentionally for what families value.</p>\n</div>',
              '<div class="stack" style="width:856px;gap:24px">\n<h2 class="title">REALM began with a conviction.</h2>\n<p class="lede">Family Capital deserves real estate investment built intentionally for what families value.</p>\n</div>')
s = re.sub(r'<aside>.*?</aside>', lambda m: '<aside>v1.3 slide 29 (“The Founding Story”), moved up next to the firm overview. Headline and lede are v1.3’s own opening sentence, split in two. Four beats on one line (CP Timeline pattern). Photo window from v2.1 (cypress) top right; text stays on Paper. Copy unchanged.</aside>', s, flags=re.S)
wr('slides/story.html', s)

# ---------- capital-four: tall cypress window under the left column ----------
s = rd('slides/capital-four.html')
if 'class="win"' not in s:
    win = (f'<img class="win" src="{CYPT}" alt="Cypress trees rising against a clear sky" style="left:0;top:470px;width:648px;height:490px">\n'
           + arcs(648, 490, 640, 1000, [760, 640, 520], [30, 40, 50], 0, 470))
    s = s.replace('<section id="capital-four">\n', '<section id="capital-four">\n' + win)
    wr('slides/capital-four.html', s)
print('done')
