---
name: cp-pitch-deck
description: Collateral Partners method for designing client pitch decks, company overviews and investor presentations with Claude Code and the Slides artifact type. Covers the round order (midfi, colour and logo, images, polish), the 1920×1080 12-column grid and slim footer, type scale, palette discipline, brand vectors, photo rules (Magnific Cinematic, no text or pattern over photos), div-grid tables, copy and compliance rules, the preview-and-review loop, and the GitHub handoff. Use whenever CP builds, restyles or reviews a deck for a client, including applying the CP design to a client's own .pptx.
---

# CP pitch deck

How Collateral Partners designs a client deck with Claude Code. Distilled from the REALM Company Overview test (Nov 2026). `references/realm-case.md` holds that case's tokens and decisions as a worked example. `references/realm-deck.css` is its complete stylesheet, usable as a starter.

## 1. Before designing

- **Read everything the client gave you:** the brief, the brand kit (palette roles, type, logo rules, vectors), CP references (Design Hub, layout file) and any existing client deck.
- **Mine a client .pptx before you redesign it:**
  - dump text, layouts and media with `scripts/dump_pptx.py`;
  - unzip `ppt/media` for its textures and drawn assets.
  The native file often has better drawn assets (brush rings, glyphs, pins) than a first redesign. Carry them over.
- **Note the palette roles.** A tertiary colour (REALM's Juniper) is reserved for its set moments (buttons, rings). Keep it out of slides unless the brand says otherwise.
- **List compliance-sensitive content up front.** Flag it in speaker notes and the handoff, and never resolve it yourself:
  - prior-entity track records;
  - fees and promote;
  - fund or strategy status;
  - projected or targeted figures.

## 2. Round order (do not skip ahead)

1. **Midfi.** Real copy, grey boxes, structure and story only.
2. **Colour and logo.** Palette, logo lockups, brand vectors.
3. **Images.** Photography and textures.
4. **Final adjustments.** Spacing, type, tables, review comments.

Each round starts from the previous round's latest published version. Before changing a deck, re-read what earlier rounds established (assets, vectors, layouts). Losing them reads as a downgrade to the client, and it happened once in the REALM test.

## 3. Grid and structure (1920×1080)

| Element | Rule |
|---|---|
| Margins | sides 88, top 72, bottom padding 120 |
| Columns | 12 × 116px, gutter 32 (pitch 148). Column *n* starts at x = 88 + (n − 1) × 148. A span of *k* columns is 148k − 32 wide |
| Content area | y 72 → 960 |
| Footer | one 30px row at bottom 44: logo · section name · page number. Never a tall band |
| Section name | lives in the footer, not in an eyebrow above the title |
| Type | Display / title / h48 / lede / text = 120 / 72 / 48 / 28 / 24. **Nothing under 24px.** Left-aligned, tabular figures |

- Place every block on grid columns (`grid-column: a / b`). When a reviewer says "narrower, push it right", move the block's start column rather than inventing an offset.
- **Dense slides:** first step the scale down one notch (72→64 titles, 28→26 ledes) and tighten margins within the grid. Then cut text slightly. Never shrink gaps until items touch: "tight" was the most common review comment.
- **Section covers** (dark): a big number + display title on the left; the topic list on the right in a solid `#3B4556`-style panel with matching rules, so the list never sits on a vector or photo.
- Layouts come from the client's references and the brand moodboard, not from generic templates. Propose new layouts when the reference material supports them.

## 4. Visual language

- **Use the brand's own vectors and textures** (rings, arcs, brush strokes, wireframes, pins, glyphs). A deck with only type and photos feels "undesigned".
- **Photos:**
  - One whole photo in a box (a "window"). No pattern, arc or texture over a photo.
  - **No text over photos or assets.** Where text must sit on an asset, give it a solid chip in the background colour.
- **Tables:** the Slides type strips table styling, so build them as **div grids**:
  - dark header row;
  - display face in the first column;
  - hairline row rules and generous cell padding;
  - the client's own column always on the same light accent band, so comparisons read the same on every slide.
- **Logos:** flat, single colour. The dark logo goes on light slides and the white logo on dark ones.
- **Covers:** if the client's native cover is strong, port it (same vectors, same composition) rather than inventing a new one.

## 5. Images (Magnific)

- **Model and settings.** Use the Cinematic model with one camera setup for the whole deck, so the set reads as one shoot. REALM used:
  - medium format, Hasselblad Planar 85mm, f/8;
  - Fuji Velvia 50, hard sunlight, barely visible grain;
  - no halation, no motion blur.
- **Download** with `creations_register_download` before fetching the file.
- **Never generate portraits of real people.** Leadership slides get real photos or an empty, marked placeholder.
- **Case studies and properties:** generated images are illustrative only. Say so in `alt` and in the handoff, and swap in the real assets before anything leaves CP.
- **Upload** each image as an artifact asset and reference it as `/_blob/<id>`. Keep a blob map (id → local file).

## 6. Copy

- **Keep the client's words.** Light trims only ("reduce text, but softly"). Don't rewrite claims.
- **No AI slop:**
  - no invented slogans or taglines;
  - no eyebrow labels;
  - no "institutional", "exclusive access", "tailored solutions";
  - no ®.
- **Speaker notes (`<aside>`)** record where each slide's content came from (e.g. "v1.3 slide 12") and any compliance flag.

## 7. Slides artifact mechanics

Full notes are in `references/slides-mechanics.md`. Essentials:
- **Files:** `project/deck.json` (order, faces, `format.shared: deck.css`), `project/deck.css`, `project/slides/<id>.html`.
- **Read before you write.** People edit in the page, so always read the latest published version before editing, and build on it.
- **Limits:**
  - 24px font floor;
  - at most 24 pinned children per box;
  - no `object-position`;
  - tables lose styling (use div grids).

## 8. Check and review loop

1. **Render locally.** `scripts/preview_deck.py` builds one static page; screenshot it with headless Edge or Chrome (`--virtual-time-budget`, or use `ONLY=` for subsets of long decks). Then make contact sheets with `scripts/sheet.py` or `scripts/pick.py`.
2. **Inspect every slide for:**
   - gaps and spacing;
   - text over images;
   - overflow and clipped text;
   - orphan words;
   - blocks off the grid;
   - footer consistency.
3. **Publish**, then work from the in-page comments. Fix each one in the source and reply in its thread with what changed. Don't resolve threads unless asked.

## 9. Handoff

- **Repo layout:**
  - `decks/<version>/project` and `assets/blobs/<id>.<ext>`;
  - `assets/blobs.json`, with fonts as `FONT:<file>` and excluded for licence reasons;
  - brand kit, photos by round, the client source files;
  - scripts;
  - `README.md` and `HANDOFF.md`.
- **HANDOFF.md** lists what was done per round, how, the design rules, the open items (compliance, portraits, illustrative images) and how to continue.
- **Push** to a **private** repo under the CP webservices GitHub account. Set a repo-local git identity (the account's noreply address); never use personal emails.
- **Process page:** an optional private artifact with *What we did / How / Process / Result*.
- **Windows:** use `\\?\` long paths in Python and `git config core.longpaths true`. Write Python with the Write tool rather than bash heredocs, which mangle backslashes.

## Final checklist

- [ ] Every slide on the 12-column grid, footer one slim row, nothing under 24px
- [ ] No tertiary colour outside its role; logos single colour
- [ ] Brand vectors present; no pattern or text over photos
- [ ] Tables as styled div grids
- [ ] No invented slogans, eyebrows or banned words; client copy intact
- [ ] Compliance items flagged in notes and handoff
- [ ] No generated portraits; illustrative images labelled
- [ ] Earlier rounds' assets carried forward
- [ ] Latest published version read before every edit
