number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))

try:
    result = number1 / number2
except ZeroDivisionError:
    print("Can not devide by zero")
else:
    print(result)