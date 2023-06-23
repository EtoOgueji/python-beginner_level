# file detection

import os

path = "C:\\Users\\Eto Ogueji\\Desktop\\poem.txt.txt"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("This location doesn't exist")