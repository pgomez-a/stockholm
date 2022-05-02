#############
# Libraries #
#############

from cryptography.fernet import Fernet
import os

################################
# Program: python gen_key.py P #
################################

if len(sys.argv) != 2:
    print("Error: (input)")

if not os.path.isfile(sys.argv[1]):
    key = Fernet.generate_key()
    with open(sys.argv[1], "wb") as f:
        f.write(key)
    print(sys.argv[1], "file has been created")
else:
    print(sys.argv[1], "file already exists")
