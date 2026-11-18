# REALM Company Overview: Claude Code deck test

Collateral Partners tested whether Claude Code can speed up pitch-deck design. The test client is REALM, a family-capital real estate firm, and the brand route is **Bold**.

This repo holds everything the test produced: five deck versions as Slides-artifact source, the image and vector assets, the source material, and the helper scripts.

Start with **[HANDOFF.md](HANDOFF.md)**. It covers the decisions, the open items and how to continue. For a short visual summary, see the [process page](https://claude.ai/artifact/7k8P9B2jUstDG5qa3wQEoE).

## Live decks

| Version | What it is | Slides | Link |
|---|---|---|---|
| **v1.4** | CP design applied to the client's v1.3 pptx. **Current.** | 45 | [open](https://claude.ai/artifact/SoSw5JL56rL63RxD51tVpg) |
| v3 | Bold layout study | 12 | [open](https://claude.ai/artifact/8YCxeTizaxHa9oAGDxDDo3) |
| v2.1 | v2 brought to CP standards | 15 | [open](https://claude.ai/artifact/JSEjbnESzBaKnm14YBfi2s) |
| v2 | Colour, logo and images on top of v1 | 12 | [open](https://claude.ai/artifact/KC29tMwhHX5pXk2MxaGJjU) |
| v1 | Midfi structure | 10 | [open](https://claude.ai/artifact/MM161RXJvQfUAHCNFrKhjW) |

The links are private Claude artifacts. Ask the owner for access.

## Layout

```
decks/<version>/project/   deck.json, deck.css, slides/*.html (Slides artifact source)
assets/blobs/              every image the decks reference, named <blob id>.<ext>
assets/blobs.json          blob id -> file path ("FONT:<file>" for fonts, which are not included)
assets/brand-kit-bold/     REALM Bold brand kit (md, pdf, logos, images)
assets/logos-original/     logo files as received
assets/photos/v2|v3|v4/    Magnific Cinematic photography and drawn vectors, by round
assets/v13-brush-rings/    brush-ring textures from the v1.3 pptx and the composed cover
source/                    v1.3 pptx and its text, brief, prompt, image direction, CP layout file
docs/process-flow.png      the test process
scripts/                   preview and audit helpers (Python)
```

## Preview a deck locally

```bash
python scripts/preview_deck.py decks/v1.4-company-overview out/v1.4
```

This writes `out/v1.4/index.html`, a static page with every slide at 1920×1080. The fonts are licensed and not in the repo. Put `Sentient-Variable.woff2` and `Geist-VariableFont_wght.ttf` in `fonts/`, or point `FONTS_DIR` at them. `ONLY=cover,overview` renders a subset.
