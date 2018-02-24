import glob
from PIL import Image
g=glob.glob("*.png")
for h in g:
  im=Image.open(h)
  width, height = im.size
  img_name=h.replace(".jpg","")+"_400_.jpg"
  #print (h,width,height)
  if width>400:
      resize_ratio=400/width
      im.thumbnail((int(width*resize_ratio),int(height*resize_ratio)), Image.ANTIALIAS)
      im.save(img_name)
  else:
      resize_ratio=1
  print (h,width,height,width*resize_ratio,height*resize_ratio,img_name)
