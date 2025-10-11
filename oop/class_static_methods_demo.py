class Calculator:
    """Calculator class demonstrating class methods and static methods."""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        Static methods don't have access to 'self' or 'cls' and behave like 
        regular functions but belong to the class's namespace.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: The sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        
        Class methods have access to the class (cls) and can access class 
        attributes and other class methods.
        
        Args:
            cls: The class itself (automatically passed)
            a (float): First number
            b (float): Second number
            
        Returns:
            float: The product of a and b
        """
        # Access class attribute through cls
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    
    @staticmethod
    def subtract(a, b):
        """
        Another static method example - subtract two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: The difference of a and b
        """
        return a - b
    
    @classmethod
    def divide(cls, a, b):
        """
        Another class method example - divide two numbers.
        
        Args:
            cls: The class itself (automatically passed)
            a (float): First number (dividend)
            b (float): Second number (divisor)
            
        Returns:
            float: The quotient of a and b
            
        Raises:
            ValueError: If attempting to divide by zero
        """
        print(f"Performing {cls.calculation_type}")
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def demonstrate_usage():
    """Function to demonstrate the usage of class and static methods."""
    
    print("=== Calculator Class Methods and Static Methods Demo ===\n")
    
    # Using static methods - can be called on class or instance
    print("1. Static Method Examples:")
    print("-" * 30)
    
    # Call static method on the class directly
    result1 = Calculator.add(10, 5)
    print(f"Calculator.add(10, 5) = {result1}")
    
    # Call static method on an instance
    calc_instance = Calculator()
    result2 = calc_instance.add(20, 15)
    print(f"calc_instance.add(20, 15) = {result2}")
    
    # Another static method
    result3 = Calculator.subtract(100, 25)
    print(f"Calculator.subtract(100, 25) = {result3}")
    
    print("\n2. Class Method Examples:")
    print("-" * 30)
    
    # Call class method on the class directly
    result4 = Calculator.multiply(8, 7)
    print(f"Calculator.multiply(8, 7) = {result4}")
    
    # Call class method on an instance
    result5 = calc_instance.multiply(12, 3)
    print(f"calc_instance.multiply(12, 3) = {result5}")
    
    # Another class method
    result6 = Calculator.divide(50, 10)
    print(f"Calculator.divide(50, 10) = {result6}")
    
    print("\n3. Accessing Class Attributes:")
    print("-" * 35)
    print(f"Class attribute value: {Calculator.calculation_type}")
    print(f"Accessed via instance: {calc_instance.calculation_type}")
    
    print("\n4. Key Differences Summary:")
    print("-" * 30)
    print("Static Methods:")
    print("  - Use @staticmethod decorator")
    print("  - No access to 'self' or 'cls'")
    print("  - Behave like regular functions")
    print("  - Can be called on class or instance")
    print("  - Don't access class/instance attributes")
    
    print("\nClass Methods:")
    print("  - Use @classmethod decorator")
    print("  - Receive 'cls' as first parameter")
    print("  - Can access class attributes and methods")
    print("  - Can be called on class or instance")
    print("  - Often used for alternative constructors")


if __name__ == "__main__":
    demonstrate_usage()