import sys
from pptx import Presentation
from pptx.util import Emu
p = Presentation(sys.argv[1])
print("size", round(Emu(p.slide_width).inches,3), round(Emu(p.slide_height).inches,3), "slides", len(p.slides))
fonts = {}
for i, s in enumerate(p.slides, 1):
    print(f"\n=== {i} [{s.slide_layout.name}]")
    for sh in s.shapes:
        k = str(sh.shape_type).split(" ")[0]
        box = f"{Emu(sh.left).inches:.1f},{Emu(sh.top).inches:.1f} {Emu(sh.width).inches:.1f}x{Emu(sh.height).inches:.1f}" if sh.width else ""
        t = ""
        if sh.has_text_frame:
            t = sh.text_frame.text.strip().replace("\n", " / ")[:160]
            for para in sh.text_frame.paragraphs:
                for r in para.runs:
                    if r.font.name: fonts[r.font.name] = fonts.get(r.font.name, 0) + 1
        if sh.has_table if hasattr(sh,'has_table') else False:
            t = "TABLE " + " | ".join(c.text for row in sh.table.rows for c in row.cells)[:200]
        if t or k in ("PICTURE","CHART","TABLE","GROUP"):
            print(f"  {k:10} {box:22} {t}")
    if s.has_notes_slide:
        n = s.notes_slide.notes_text_frame.text.strip().replace("\n"," / ")
        if n: print("  NOTES:", n[:200])
print("\nfonts", sorted(fonts.items(), key=lambda x:-x[1])[:8])
