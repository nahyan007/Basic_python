# logical operators (and, or, not) = used to check if two or more conditional statement

temp = int(input("What temperature is today?: "))

if (temp > 34):
    print("Its very hot today drink water")
elif (temp >= 26 and temp <=34 ):
    print("Its hot today drink some water")
elif (temp == 20 or temp >= 25):
    print("its a nice warm weather go outside")
elif not(temp <12 or temp >=20 ):
    print("its a bit chilly wear a jacket")
else:
    print("its freezing")
    