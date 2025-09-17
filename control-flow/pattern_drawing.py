# This program draws a size of the pattern using asterisks.

while True:
    try:
        number_lines = int(input("Enter the size of the pattern: ").strip())
        if number_lines > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

for _ in range(number_lines):
    print('*' * number_lines)