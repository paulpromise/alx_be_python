#Use the case to write a calculator that performs different operations based on user input.


num1 = float(input("Enter the first number: ").strip())
num2 = float(input("Enter the second number: ").strip())
operation = input("Choose the operation (+, -, *, /): ").strip().lower()
match operation:
    case "+":
        result = num1 + num2
        print(f"The result of adding {num1} and {num2} is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result of subtracting {num2} from {num1} is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result of multiplying {num1} and {num2} is {result}.")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of dividing {num1} by {num2} is {result}.")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please choose add, subtract, multiply, or divide.")