# Worked example: REALM Company Overview (Nov 2026)

- **Client:** REALM, family-capital real estate. Brand route: **Bold**.
- **Repo:** `webservices-at-collateral/realm-company-overview` (private).
- **Stylesheet:** the full v1.4 file is `realm-deck.css`, next to this file.

## Tokens

| Token | Value | Role |
|---|---|---|
| Paper | `#F6F3EE` | light background |
| Harbor | `#1D2430` | ink, dark slides, table headers |
| Slate | `#8693A6` | working accent; `#55627A` for small text on Paper |
| Stone | `#B5B1AB` | rules |
| Mist | `#ECE7E0` | alternate light background |
| Panel | `#3B4556` | section-cover topic panel, rules on dark |
| Juniper | `#818A75` | tertiary: buttons and rings only, **not used in the deck** |

**Type:** Sentient Light for display and titles; Geist for text.

## Rounds

| Round | Slides | Lesson |
|---|---|---|
| v1 midfi | 10 | Real copy in grey boxes made the story review fast |
| v2 | 12 | Palette, logo, Magnific photography, ring vectors |
| v2.1 | 15 | CP standards: grid, footer, type scale |
| v3 | 12 | Layout study, second photography set |
| v1.4 | 45 | Client's v1.3 pptx rebuilt in CP design. The first pass lost v2.1's assets ("we downgraded"), so they were restored |

## Review comments and the fix that worked

| Comment | Fix |
|---|---|
| "too undesigned, where are the brand vectors?" | Brought back the textures, wireframe rings, glyphs and pins from the brand kit and the native pptx |
| "less AI slop" | Removed invented lines and eyebrows. Kept the client's copy |
| "avoid text over images" | Photos moved into windows; text gets solid chips |
| "tables prettier" | Div-grid tables: Harbor header, Sentient first column, REALM column on a Slate tint |
| "inner covers: background on topics, #3B4556" | Section-cover topic list in a `#3B4556` panel with matching rules |
| "no pattern on the images" | Regenerated the photos clean; no arcs over photos |
| "reduce width, push right" | Moved the block's start column on the grid |
| "weird arrows" | Replaced the arrows with SVG stage lines |
| "tight" (case studies) | Looser template: shorter photo, wider value column (`1fr 1fr 1.35fr`), larger gaps |
| "the reference cover is better" | Ported v1.3 page 1: the painted brush rings, rising from the bottom-right corner |

## Magnific prompt shape (case-study photo)

> Exterior of a [building type] in [setting], [time of day], architectural photograph, no people, no text.

Use `cinematicControls`:
- medium-format, hasselblad-planar, 85mm, f/8;
- fuji-velvia-50, hard-sunlight, barely-visible-shadow-grain;
- halation none, motionBlur none.

## Still open at handoff

- Compliance:
  - prior-entity "+$6B" record;
  - fees and double promote;
  - strategy status table;
  - projected figures.
- Real leadership portraits.
- Real case-study photos (the seven current ones are illustrative).
