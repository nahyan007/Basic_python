import os

path = "35.delete_a_file.txt"

try:
    os.remove(path)
    print(path + " was deleted")
except FileNotFoundError:
    print("that file does not exist")