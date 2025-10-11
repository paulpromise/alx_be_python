#!/usr/bin/env python3

from class_static_methods_demo import Calculator


def main():
    """Simple demonstration of the Calculator's class and static methods."""
    
    print("Calculator Class and Static Methods Demo")
    print("=" * 40)
    
    # Test static method - add
    print("Static Method - add:")
    result1 = Calculator.add(10, 5)
    print(f"Calculator.add(10, 5) = {result1}")
    
    # Test class method - multiply
    print("\nClass Method - multiply:")
    result2 = Calculator.multiply(6, 7)
    print(f"Calculator.multiply(6, 7) = {result2}")
    
    # Test calling methods from an instance
    print("\nCalling from instance:")
    calc = Calculator()
    
    result3 = calc.add(8, 12)
    print(f"calc.add(8, 12) = {result3}")
    
    result4 = calc.multiply(4, 9)
    print(f"calc.multiply(4, 9) = {result4}")


if __name__ == "__main__":
    main()