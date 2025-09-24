from datetime import datetime, timedelta


def display_current_datetime():
    now = datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    future_date = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=future_date)

    return f"Future date: {future_date.strftime('%Y-%m-%d')}"


display_current_datetime()
print(calculate_future_date())
