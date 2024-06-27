try:
    with open("31.read a file.txt") as file:
        print (file.read())
except FileNotFoundError:
    print("That file does not exist")