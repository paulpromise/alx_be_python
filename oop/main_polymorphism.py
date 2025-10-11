#!/usr/bin/env python3

from polymorphism_demo import Shape, Rectangle, Circle


def main():
    """
    Main function demonstrating polymorphism by creating instances of 
    Rectangle and Circle, and invoking their area() method.
    """
    
    # Create instances of Rectangle and Circle
    rectangle = Rectangle(10, 5)
    circle = Circle(7)
    
    # Demonstrate polymorphism - same interface, different implementations
    shapes = [rectangle, circle]
    
    print("Demonstrating Polymorphism:")
    print("-" * 30)
    
    for shape in shapes:
        # Each shape calculates area according to its specific implementation
        area = shape.area()
        shape_type = type(shape).__name__
        print(f"{shape_type} area: {area:.2f}")


if __name__ == "__main__":
    main()