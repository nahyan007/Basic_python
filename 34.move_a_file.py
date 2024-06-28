import os

source = "C:\\Users\\Nahian\\Desktop\\34.move_a_file.txt"
destination = "34.move_a_file.txt"

try:
    if os.path.exists(destination):
        print("There is already a file")
    else:
        os.replace(source, destination)
        print(source + " already moved")
except FileNotFoundError:
    print(source + " was not found")