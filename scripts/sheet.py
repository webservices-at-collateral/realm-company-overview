import sys
from PIL import Image
src, out, start, count = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
im = Image.open(src)
n = im.height // 1080
cols = 2; w, h = 960, 540
idx = list(range(start, min(start+count, n)))
rows = (len(idx)+cols-1)//cols
sheet = Image.new('RGB', (cols*w + (cols+1)*12, rows*h + (rows+1)*12), (90,90,90))
for k, i in enumerate(idx):
    s = im.crop((0, i*1080, 1920, (i+1)*1080)).resize((w, h), Image.LANCZOS)
    sheet.paste(s, (12 + (k%cols)*(w+12), 12 + (k//cols)*(h+12)))
sheet.save(out)
