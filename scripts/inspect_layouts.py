import sys
from pptx import Presentation
from pptx.util import Emu

p = Presentation(sys.argv[1])
print("size", round(Emu(p.slide_width).inches, 3), round(Emu(p.slide_height).inches, 3), "slides", len(p.slides))
print("masters", len(p.slide_masters), "layouts", [l.name for m in p.slide_masters for l in m.slide_layouts][:30])
fonts = {}
for i, s in enumerate(p.slides, 1):
    texts, kinds = [], {}
    for sh in s.shapes:
        k = str(sh.shape_type).split(" ")[0]
        kinds[k] = kinds.get(k, 0) + 1
        if sh.has_text_frame:
            t = sh.text_frame.text.strip().replace("\n", " / ")
            if t:
                texts.append(t[:50])
            for para in sh.text_frame.paragraphs:
                for r in para.runs:
                    if r.font.name:
                        fonts[r.font.name] = fonts.get(r.font.name, 0) + 1
    print(f"{i:02d} [{s.slide_layout.name}] {kinds} :: {' | '.join(texts[:5])[:220]}")
print("fonts", sorted(fonts.items(), key=lambda x: -x[1])[:8])
