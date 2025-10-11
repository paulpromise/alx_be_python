#!/usr/bin/env python3

from polymorphism_demo import Shape, Rectangle, Circle


def main():
    """Demonstrate polymorphism with Shape, Rectangle, and Circle classes."""
    
    # Create instances of Rectangle and Circle
    rectangle = Rectangle(10, 5)
    circle = Circle(7)
    
    # List of shapes to demonstrate polymorphism
    shapes = [rectangle, circle]
    
    print("Polymorphism Demo: Shape Area Calculations")
    print("=" * 45)
    
    # Demonstrate polymorphism - same method call, different implementations
    for shape in shapes:
        if isinstance(shape, Rectangle):
            print(f"Rectangle (Length: {shape.length}, Width: {shape.width})")
            print(f"Area: {shape.area():.2f}")
        elif isinstance(shape, Circle):
            print(f"Circle (Radius: {shape.radius})")
            print(f"Area: {shape.area():.2f}")
        print("-" * 30)
    
    # Demonstrate that calling area() method works polymorphically
    print("Polymorphic behavior:")
    for i, shape in enumerate(shapes, 1):
        print(f"Shape {i} area: {shape.area():.2f}")
    
    # Demonstrate that base Shape class raises NotImplementedError
    print("\nTesting base Shape class:")
    try:
        base_shape = Shape()
        base_shape.area()
    except NotImplementedError as e:
        print(f"NotImplementedError caught: {e}")


if __name__ == "__main__":
    main()