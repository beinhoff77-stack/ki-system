import sys
from PIL import Image
ims=[Image.open(f) for f in sys.argv[2:]]
c=Image.new('RGB',(sum(i.width for i in ims)+8*(len(ims)-1),ims[0].height),'white'); x=0
for i in ims: c.paste(i,(x,0)); x+=i.width+8
c.save(sys.argv[1])
