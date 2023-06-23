#deleting files

import os

path = "empty_folder"

try:
    os.remove(path)
except FileNotFoundError:
    print("That file/folder was not found")
except PermissionError:
    print("you don't have the permission to do that")
else:
    print(path+" was deleted")