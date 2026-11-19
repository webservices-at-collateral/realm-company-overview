import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
src,out=sys.argv[1],sys.argv[2]; idx=[int(x) for x in sys.argv[3].split(',')]
im=Image.open(src); w,h=960,540; rows=(len(idx)+1)//2
sheet=Image.new('RGB',(2*w+36,rows*(h+12)+12),(90,90,90))
for k,i in enumerate(idx):
    s=im.crop((0,i*1080,1920,(i+1)*1080)).resize((w,h))
    sheet.paste(s,(12+(k%2)*(w+12),12+(k//2)*(h+12)))
sheet.save(out)
