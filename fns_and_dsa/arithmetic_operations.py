def perform_operation(num1, num2, operation):
    operation = operation.lower()
    
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero error"
    else:
        return "Invalid operation"

    return result