task_description = input("Enter your task: ")

priority = int(input("Priority ('High', 'Medium', 'Low') : "))


time_bound = input("Is it time-bound? (yes/no): ").strip().lower() == "yes"

match priority:
    case "High":
        if time_bound == "yes":
            print(
                "Reminder: 'Finish project report' is a high priority task that requires immediate attention today!"
            )

    case "Medium":
        if time_bound == "yes":
            print(
                "Reminder: 'Prepare presentation' is a medium priority task that needs to be done this week!"
            )

    case "Low":
        if time_bound == "yes":
            print(
                "Note: 'Read a book' is a low priority task. Consider completing it when you have free time"
            )
    case _:
        priority_str = "Unknown"
