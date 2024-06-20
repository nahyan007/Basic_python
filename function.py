# function = a block of code which is executed only when it is called.

def car(brand, model, year):
    print("its a "+model.upper()+" "+str(year)+" year edition model from "+brand.upper())
    


car(
    input("Please enter your car brand name: "),
    input("Please enter your car model name: "),
    input("Please enter your car model year: "),
    )
    