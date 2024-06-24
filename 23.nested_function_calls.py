# nested functions calls = Function calls inside the function calls. 
# innermost function calls are resolved first. 
# return value is used as argument for the function


# num = input("Please enter a positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("Please enter a positive number: ")))))