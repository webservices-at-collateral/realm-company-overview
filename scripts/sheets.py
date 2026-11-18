import sys, os, glob
import pymupdf

src = sys.argv[1]
out = sys.argv[2]
os.makedirs(out, exist_ok=True)
COLS, ROWS, TW = 5, 4, 480
for f in sorted(glob.glob(os.path.join(src, "*.pdf"))):
    name = os.path.splitext(os.path.basename(f))[0]
    doc = pymupdf.open(f)
    n = len(doc)
    per = COLS * ROWS
    sheets = (n + per - 1) // per
    print(name, "pages:", n, "sheets:", min(sheets, 2))
    for sh in range(min(sheets, 2)):
        idxs = list(range(sh * per, min(n, (sh + 1) * per)))
        thumbs = []
        for i in idxs:
            pg = doc[i]
            z = TW / pg.rect.width
            pix = pg.get_pixmap(matrix=pymupdf.Matrix(z, z))
            thumbs.append(pix)
        th = thumbs[0].height
        W = COLS * TW + (COLS + 1) * 8
        H = ROWS * th + (ROWS + 1) * 8
        sheet = pymupdf.Pixmap(pymupdf.csRGB, pymupdf.IRect(0, 0, W, H), False)
        sheet.set_rect(sheet.irect, (200, 200, 200))
        for k, pix in enumerate(thumbs):
            r, c = divmod(k, COLS)
            x = 8 + c * (TW + 8)
            y = 8 + r * (th + 8)
            if pix.alpha:
                pix = pymupdf.Pixmap(pix, 0)
            pix.set_origin(x, y)
            sheet.copy(pix, pymupdf.IRect(x, y, x + pix.width, y + pix.height))
        safe = name.replace(" ", "_")
        sheet.save(os.path.join(out, f"{safe}_s{sh+1}.png"))
