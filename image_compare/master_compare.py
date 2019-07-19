#!/usr/bin/env python

#compare a master image to a series of other images, calculate the hamming distance as a measure of image similarity
#based on http://www.hackerfactor.com/blog/?/archives/432-Looks-Like-It.html

import shutil
import sys, os
import glob
from PIL import Image
#from PIL import ImageFont
#from PIL import ImageDraw

def hammingDistance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(bool(ord(ch1) - ord(ch2)) for ch1, ch2 in zip(s1, s2))

if (len(sys.argv) != 2):
  sys.exit("syntax master_compare.py masterimage")
else:
  imgmast = sys.argv[1]

images = glob.glob('2015*.jpg')
images.insert(0, imgmast)

#calculate hexadecimal hash for images
metric = []
for img in (images):
  image = Image.open(img)

  image = image.crop((0, 0, 1280, 960))
  #crop = 'crop_' + os.path.splitext(img)[0] + '.jpg'
  #image.save(crop)

  image = image.resize((8, 8), Image.ANTIALIAS)
  image = image.convert("L")
  #small = 'small_' + os.path.splitext(img)[0] + '.jpg'
  #image.save(small)
  
  pixels = list(image.getdata())
  avg = sum(pixels) / len(pixels)

  #bw = image.point(lambda i: 0 if (i < avg) else 255)
  #bwimg = 'bw_' + os.path.splitext(img)[0] + '.jpg'
  #bw.save(bwimg)

  bits = "".join(map(lambda pixel: '1' if (pixel < avg) else '0', pixels))  # '00010100...'
  hexhash = int(bits, 2).__format__('016x').upper()
  metric.append(hexhash)

#calculate hamming distance for master compared to all and output
print 'master:', imgmast, 'hash:', metric[0]
for idx, img in enumerate(images):
  hamdist = hammingDistance(metric[0], metric[idx])
  if  idx >= 1:
    print idx, 'image:', img, 'hash:', metric[idx], 'hamdist:', hamdist
