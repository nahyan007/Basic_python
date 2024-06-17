# if statement = a block of code that will execute its condition is true

age = int(input("what is your age ? "))

if age == 100:
    print("damn you are old")

elif age >= 18:
    print("you are adult")
    
elif age <0:
    print("you are not born yet")
else:
    print("you are child")