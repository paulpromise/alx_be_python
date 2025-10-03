def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    return "Division by zero error"

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def floor_divide(x, y):
    if y != 0:
        return x // y
    return "Division by zero error"
