import sys
from PIL import Image
'''for i in range(100,102):
    if (i<10):
        s='0'+str(i)
    else:
        s=str(i)'''
images = [Image.open(x) for x in ['./AR_cropped_sketches/Mp-002-1-sz1.jpg', './AR_cropped_sketches/Mp-003-1-sz1.jpg']]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('mfmm1'+'.jpg')
