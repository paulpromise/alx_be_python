Task = input("Enter your task: ")

Priority = int(input("Priority (high/medium/low): "))


Time_Bound = input("Is it time-bound? (yes/no): ").strip().lower() == "yes"

match Priority:
    case "high":
        if Time_Bound == "yes":
            print(
                "Reminder: 'Finish project report' is a high priority task that requires immediate attention today!"
            )
        else:
            print(
                "Reminder: 'Finish project report' is a high priority task. Please complete it as soon as possible."
            )

    case "medium":
        if Time_Bound == "yes":
            print(
                "Reminder: 'Prepare presentation' is a medium priority task that needs to be done this week!"
            )
        else:
            print(
                "Reminder: 'Prepare presentation' is a medium priority task. Please complete it when you can."
            )

    case "low":
        if Time_Bound == "yes":
            print(
                "Reminder: 'Read a book' is a low priority task that can be done anytime."
            )
        else:
            print(
                "Reminder: 'Read a book' is a low priority task. Feel free to do it at your leisure."
            )
    case _:
        priority_str = "Unknown"
