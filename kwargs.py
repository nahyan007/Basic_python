# **kwargs = parameter that will pack all arguments into a dictionary useful so that a function can accept a varying amount of arguments

def name(**kwargs):
    print("its a ", end= " ")
    for key , value in kwargs.items():
        print(value, end= " ")
        

name(first_name="toyotas",middle_name="supra",last_name="mk4")