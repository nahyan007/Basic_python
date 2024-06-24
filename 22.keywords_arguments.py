# keywords arguments = arguments preceded by an identifier when we pass them to a function. The order of the arguments does not matter, unlike positional arguments python knows the names of the arguments that our function receives


def hello(first ,middle, last):
    print("Hello "+first.capitalize()+" "+middle.capitalize()+" "+last.capitalize())
    
    
hello(last="avid",first="mr",middle="nahian")