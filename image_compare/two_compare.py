#!/usr/bin/env python

#based on http://www.hackerfactor.com/blog/?/archives/432-Looks-Like-It.html

import shutil
import sys, os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def hammingDistance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(bool(ord(ch1) - ord(ch2)) for ch1, ch2 in zip(s1, s2))

if (len(sys.argv) != 3):
  sys.exit("syntax test.py imagefile1 imagefile2")
else:
  img1 = sys.argv[1]
  img2 = sys.argv[2]

#calculate hexadcimal hash for images
metric = []
for img in (img1, img2):
  image = Image.open(img)

  image = image.crop((0, 0, 1280, 960))
  image = image.resize((8, 8), Image.ANTIALIAS)
  image = image.convert("L")

  pixels = list(image.getdata())
  avg = sum(pixels) / len(pixels)

  bits = "".join(map(lambda pixel: '1' if (pixel < avg) else '0', pixels))  # '00010100...'
  hexhash = int(bits, 2).__format__('016x').upper()
  metric.append(hexhash)

hamdist = hammingDistance(metric[0], metric[1])
print 'img1: ', img1
print 'hash: ', metric[0]
print 'img2: ', img2
print 'hash: ', metric[1]
print 'hamdist: ', hamdist
