# Using For loops to Create a Multiplication Table
# This program generates a multiplication table for numbers 1 through 10.

number = int(input("Enter a number to see its multiplication table: ").strip())

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")