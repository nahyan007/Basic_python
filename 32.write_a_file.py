with open("32.write_a_file.txt", "w") as file:
    file.write("hey \nthis is a test file \nand \nit's created by python\nw mood can overwrite any text given in the field")
    
    
with open("32.write_a_file.txt", "a") as file:
    file.write("\n\n\nmood a can append text to the file ")
    
    
# mood W = write file or overwrite file
# mood a = append file
# mood r = read file(its a default no need to write this)