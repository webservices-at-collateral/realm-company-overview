# Handoff: REALM Company Overview

**State on 18 Nov 2026:** v1.4 is the working deck, 45 slides plus one hidden guides slide. It follows the client's v1.3 content and runs on the CP grid and the REALM Bold brand. It still needs compliance review, real portraits and real case photos before it goes out.

## 1. What was done

| Round | Output | What changed |
|---|---|---|
| v1 | Midfi, 10 slides | Story and structure only: grey boxes, real copy |
| v2 | 12 slides | Bold palette, logo, Magnific photography, brand vectors (rings, arcs) |
| v2.1 | 15 slides | Brought to CP standards: grid, footer, type scale, Design Hub rules |
| v3 | 12 slides | Layout study with new image pairs (pool, ripple, cypress) |
| **v1.4** | **45 slides** | **The client's v1.3 pptx rebuilt in the CP design, with what v2.1 learned** |

v1.4 rounds, in order:

1. Content mapped from v1.3.
2. The tall footer fixed.
3. Margins tightened, and the type scale stepped down one notch so dense slides could breathe.
4. The v2.1 assets restored after a downgrade.
5. Tables restyled.
6. Photos regenerated without patterns.
7. Every artifact comment addressed: spacing, widths, arrows, text length.
8. Cover rebuilt from v1.3 page 1. The closing slide stays in the v1.4 design (decided not to rebuild it from v1.3 page 31).

## 2. How it was done

- **Claude Code + the Slides artifact type.** Each deck is HTML slides plus one shared `deck.css`, published as a private claude.ai artifact. Reviewers comment on slides in the page, and Claude replies in the same thread and fixes the source.
- **Magnific (Cinematic model)** for photography, always with the same camera settings so the set stays consistent:
  - medium format, Hasselblad Planar 85mm, f/8;
  - Fuji Velvia 50, hard sunlight, barely visible grain;
  - no halation, no motion blur.
- **Local preview:** `scripts/preview_deck.py`, then a headless Edge screenshot, then contact sheets (`pick.py`, `sheet.py`). Every pass was checked visually before publishing.
- **Sources:** brief, the REALM Bold brand kit, the CP Design Hub and layout file, the brand platform site's Bold+ moodboard, and the v1.3 pptx. The v1.3 brush textures were extracted from the pptx itself.

## 3. Design rules in the deck

| Rule | Value |
|---|---|
| Canvas | 1920×1080 |
| Margins | sides 88, top 72, bottom 120 |
| Grid | 12 columns of 116px, gutter 32. Column *n* starts at x = 88 + (n−1)·148 |
| Footer | one 30px row at bottom 44: logo · section · page number |
| Type | Sentient Light for headings, Geist for text. Scale 120 / 72 / 48 / 28 / 24. Nothing under 24px |
| Palette | Paper `#F6F3EE`, Harbor `#1D2430`, Slate `#8693A6`, Stone `#B5B1AB`. Section-cover chips `#3B4556` |
| Juniper `#818A75` | Tertiary. Buttons and rings only, so it is kept out of the deck |
| Images | No pattern or arcs over photos. No text over photos. Where text must sit on an asset, it gets a solid chip in the background colour |
| Tables | Built as div grids, because the Slides type strips table styling |

**Copy rules:** no invented slogans, no eyebrow labels, no "institutional", "exclusive access" or "tailored solutions", no ®.

## 4. Open items

1. **Compliance.** Flagged, not resolved:
   - the prior-entity "+$6B" track record;
   - fees and double promote;
   - the strategy status table;
   - every projected figure.
2. **Portraits.** The leadership slide needs real photos. No portraits were generated, on purpose.
3. **Case-study photos.** All seven are illustrative Magnific images. Replace them with the real properties.
4. **Fonts.** Not in the repo (licence). Install them locally to preview.
5. **v1 assets.** Seven v1 images exist only in the v1 artifact. The v1 deck's local preview shows gaps.

## 5. How to continue

- **To edit the live deck:** open the v1.4 artifact and comment, or ask Claude to change a slide. Claude reads the latest published version first, because edits made in the page are saved there.
- **To fork it into a new deck:** copy `decks/v1.4-company-overview/project` and keep `deck.css`. All layout lives in its classes and the grid above.
- **To add images:** use the same Magnific settings as above, then upload each as an artifact asset and reference it as `/_blob/<id>`. Record it in `assets/blobs.json`.

## 6. Learnings for CP

- Midfi first, then colour, then images, then polish. The order held. Skipping ahead caused rework, as when v1.4's first pass lost v2.1's assets.
- One shared stylesheet with a grid made 45 slides consistent and cheap to retune. Margins and the type scale changed deck-wide in one edit.
- In-page comments are the fastest review loop: one comment, one fix, one reply.
- Generated images must look clearly illustrative. Put real people and real properties in before anything leaves CP.
