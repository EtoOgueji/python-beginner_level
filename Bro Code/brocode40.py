# deleting folders

import os
import shutil

path = "empty_folder"

try:
    os.remove(path)
    # os.rmdir(path): will delete directory

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to delete that")

except OSError:
    printf("You cannot delete that using that function")
else:
    print(path+" was deleted")