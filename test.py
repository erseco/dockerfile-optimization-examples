#!/usr/bin/env python

import sys
import os
import whois
from PIL import Image, ImageFilter
import cryptography
from cryptography.fernet import Fernet

# Whois part
parameter = "fsf.org"
domain = whois.query(parameter)
print(domain.__dict__)
print(domain.expiration_date)

# Pillow part
print("Original image: %d" % os.stat("Lenna.png").st_size)
original = Image.open("Lenna.png")
blurred = original.filter(ImageFilter.BLUR)
blurred.save("Lenna-blurred.png")
print("Blurred image: %d" % os.stat("Lenna-blurred.png").st_size)

# Criptography part
key = Fernet.generate_key()
message = "my deep dark secret".encode()
f = Fernet(key)
encrypted = f.encrypt(message)
decrypted = f.decrypt(encrypted)
print(message == decrypted)
print(encrypted)
