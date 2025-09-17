# This program draws a size of the pattern using asterisks.


# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop for columns
    for col in range(size):
        print("*", end="")  # print star without new line
    print()  # move to the next line after finishing one row
    row += 1
