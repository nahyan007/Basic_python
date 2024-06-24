import os

path = "C:\\Users\\Nahian\\Desktop\\test"

if os.path.exists(path):
    print("this path exists")
    if os.path.isfile(path):
        print("this is a file")
    elif os.path.isdir(path):
        print("this is a folder")
else:
    print("this path doesn't exist")