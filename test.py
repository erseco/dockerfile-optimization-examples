#!/usr/bin/env python

# This code blurr the "Lenna.png" image file

import os
from PIL import Image, ImageFilter

# Pillow part
in_file = "Lenna.png"
out_file = "Lenna-blurred.png"

original = Image.open(in_file)
blurred = original.filter(ImageFilter.BLUR)
blurred.save(out_file)

print("Original image: %d" % os.stat(in_file).st_size)
print("Blurred image: %d" % os.stat(out_file).st_size)
