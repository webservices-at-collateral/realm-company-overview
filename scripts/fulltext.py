import sys
from pptx import Presentation
p = Presentation(sys.argv[1])
out = open(sys.argv[2], "w", encoding="utf-8")
for i, s in enumerate(p.slides, 1):
    out.write(f"\n=== {i}\n")
    items = []
    for sh in s.shapes:
        if sh.has_text_frame and sh.text_frame.text.strip():
            items.append((round(sh.top/914400,1), round(sh.left/914400,1), sh.text_frame.text.strip().replace("\n"," / ")))
    for t,l,x in sorted(items):
        if x.isdigit() and t>6.5: continue
        out.write(f"[{l},{t}] {x}\n")
    if s.has_notes_slide and s.notes_slide.notes_text_frame.text.strip():
        out.write("NOTES: "+s.notes_slide.notes_text_frame.text.strip().replace("\n"," / ")+"\n")
