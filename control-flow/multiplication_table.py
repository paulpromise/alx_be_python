# Using For loops to Create a Multiplication Table
# This program generates a multiplication table for numbers 1 through 10.

number = int(input("Enter a number to see its multiplication table: ").strip())

for n in range(1, 11):
    result = number * n
    print(f"{number} x {n} = {result}")