# except = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    dominator = int(input("Enter a number to divide by: "))
    result = numerator / dominator
except ZeroDivisionError as e:
    print(e)
    print("you can't divide by zero")
except ValueError as e:
    print(e)
    print("Please enter only number")
except Exception as e:
    print(e)
    print("something went wrong -_-")
else:
    print(result)
finally:
    print("error caught or not ,it will always be executed")