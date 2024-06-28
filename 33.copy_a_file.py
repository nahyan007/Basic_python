# copyfile()= copies contents of a file
# copy()    = copyfile()+ permissions mood + destination can be a directory
# copy2()   = copy()+ copies metadata( file's creation and modification times)

import shutil

shutil.copyfile("32.write_a_file.txt","33.copy_a_file.txt") #source , destination

with open("33.copy_a_file.txt", "a") as file:
    print(file.write("\n\n\n33.copy_a_file.txt is a copied file from 32.write_a_file.txt"))