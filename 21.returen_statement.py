# return statement = function send python values/objects back to caller . these values/objects are known as the function's return value

def multiply(num1, num2):
    result = num1 * num2
    print(str(num1)+" * "+ str(num2)+" = "+ str(result))
    return result

multiply(int(input("Please enter first number: ")),
         int(input("Please enter second number: ")))
    