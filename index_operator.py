# index operator [] = gives access to a sequence's element (str,list, tuples)

name = "supra MK4"

if (name[0].islower()):
    name = name.capitalize()
print(name)

# first_name = name[0:5].upper()
# short hand
first_name = name[:5].upper()
last_name = name[-3:].lower()

print(first_name)
print(last_name)
    