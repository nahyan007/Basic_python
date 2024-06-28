import os

# path = "35.delete_a_file.txt"

# try:
#     os.remove(path)
#     print(path + " was deleted")
# except FileNotFoundError:
#     print("that file does not exist")
    

# delete a folder

path = "empty_folder"

try:
    os.rmdir(path)
except FileNotFoundError:
    print("that folder does not exist")
except PermissionError:
    print("not allowed to delete")
else:
    print(path + " was deleted")