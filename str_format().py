# str format() = optional method that gives users more control when displaying output

# animal = "cow"
# item = "moon"

# print("The "+str(animal)+" Jumped over the "+str(item))  #terminal:The cow Jumped over the moon

# print("The {} jumped over the {}".format(animal, item)) #terminal:The cow Jumped over the moon

# print("The {1} jumped over the {0}".format(animal, item)) #terminal:The moon jumped over the cow

# print("The {1} jumped over the {1}".format(animal, item)) #positional arguments
# or
# print("The {item} jumped over the {item}".format(animal="cow", item="moon")) #keywords arguments
#terminal:The moon jumped over the moon

# animal = "cow"
# item = "moon"

# text= "The {} jumped over the {}"
# print(text.format(animal, item))

# ==================================================================

# name = "supra"

# print("thats a {}".format(name))
# print("thats a {:10} ,brooo".format(name)) #def left padding
# print("thats a {:<10} ,brooo".format(name)) # left padding
# print("thats a {:>10} ,brooo".format(name)) # right padding
# print("thats a {:^10} ,brooo".format(name)) # center padding


# ==================================================================



number = 42432552

# print("the number is {:.2f}".format(number)) #2 digit 
# print("the number is {:.3f}".format(number)) #3 digit. round
# print("the number is {:,}".format(number)) #div by comma
# print("the number is {:b}".format(number)) #convert binary
# print("the number is {:o}".format(number)) #convert octal
# print("the number is {:X}".format(number)) #convert hexadecimal
print("the number is {:E}".format(number)) #convert scientific notation