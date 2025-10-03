def safe_divide(numerator, denominator):
    """Performs division and handles division by zero."""
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"The result of the division is: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
