#############
# Libraries #
#############

from cryptography.fernet import Fernet
import sys
import os

#####################################
# Program: python3 decrypt.py S KEY #
#####################################

if len(sys.argv) != 3:
    print("Error: (input)")
    exit(1)

try:
    key = Fernet(sys.argv[2].encode())
except:
    print("Error: (key) invalid key")
    exit(1)

files = os.listdir("/home/infection/")

with open("wannacry.txt", "rb") as f:
    extensions = f.read()
extensions = extensions.split()

for item in files:
    item_ext = os.path.splitext(item)
    if item_ext[1] == ".ft":
        item = item_ext[0]
        item_ext = os.path.splitext(item)[1]
        if item_ext.encode() in extensions:
            with open("/home/infection/" + item + ".ft", "rb") as f:
                content = f.read()
            with open("/home/infection/" + item, "wb") as f:
                f.write(key.decrypt(content))
            os.remove("/home/infection/" + item + ".ft")
            if sys.argv[1] != "S":
                print("/home/infection/" + item + ".ft  ->  /home/infection/" + item)
        else:
            os.rename("/home/infection/" + item + ".ft", "/home/infection/" + item)
            if sys.argv[1] != "S":
                print("/home/infection/" + item + ".ft  ->  /home/infection/" + item)
