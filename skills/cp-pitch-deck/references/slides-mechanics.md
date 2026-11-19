# Slides artifact mechanics

Notes from building five decks with the Slides artifact type. The type's own `SKILL.md` and `artifact-type/reference/*.md` (published with every Slides artifact) are the source of truth. Read them when anything here disagrees.

## Create and update

- **Create:** publish with the Slides `type_url`, a `title`, no files, and `auto_open: "after_first_write"`. Then publish data files to the returned `url`.
- **Update:** publish to the deck's `url` with `root` set to the local folder that holds `project/`, and `files` mapping each `project/...` path.
- **Read first, every time.** The editor saves people's edits as new versions, so read the deck before you change it:
  - `action: "read"` with `paths` for the files you will touch;
  - or list `scope: "files"` to see the version id.
  A publish built on a stale copy overwrites their work. If the publish result warns about a newer save, merge it and republish.

## Files

```
project/deck.json         { "v": 5, "order": [...slide ids], "faces": {...}, "lists": "css", "format": { "shared": "deck.css" } }
project/deck.css          every class the slides use; tokens in :root
project/slides/<id>.html  one <section id="<id>"> per file, <aside> = speaker notes
```

- **Hidden slides:** `<section ... hidden>`. A hidden `guides` slide showing the grid is useful during design.
- **Page numbers:** `counter-increment: page` on `section`, and `.pnum::after { content: counter(page) }`.

## Assets

- **Upload:** publish with `url`, `asset: true`, and `file_path` (or up to 25 `file_paths`). Reference each result as `/_blob/<id>` in HTML or CSS.
- **Fonts:** upload them the same way and declare them in `deck.json` `faces`.
- **Blob map:** keep a local `blobmap.json` (id → local file) so previews and the handoff repo can resolve every image.

## Limits that shaped the CSS

- **Text floor:** nothing under 24px. The editor flags smaller text.
- **Children:** at most 24 absolutely positioned (pinned) children per box. Group them.
- **No `object-position`:** crop the image file itself, or size the box to the crop you want.
- **Tables:** `<table>` loses most styling, so use div grids (`.dt`, `.dt-row`, `.dt-c` in `realm-deck.css`).
- **Vectors:** inline SVG works well for drawn assets (rings, glyphs, pins, stage lines). Keep paths short, and use images for heavy art.

## Comments

- **Reading:** read threads with `ArtifactComments`. Each comment is anchored to a slide or element.
- **Replying:** reply in the same thread, saying what changed. Don't resolve threads unless the person asks, and don't reply to a thread twice.
