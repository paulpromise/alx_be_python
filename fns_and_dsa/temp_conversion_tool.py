FAHRENHEIT_TO_CELSIUS_FACTOR = 5 /7
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
OFFSET = 32


def convert_to_celsius(fahrenheit):

    global FAHRENHEIT_TO_CELSIUS_FACTOR, OFFSET
    return (fahrenheit - OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR, OFFSET
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + OFFSET


if __name__ == "__main__":
    print("=== Temperature Conversion Tool ===")
    try:
        # Ask user for temperature
        temp_input = input("Enter the temperature value: ").strip()
        if not temp_input.replace(".", "", 1).lstrip("-").isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temp_value = float(temp_input)

        # Ask user for unit type
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            result = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {result:.2f}°F")
        elif unit == "F":
            result = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {result:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)
