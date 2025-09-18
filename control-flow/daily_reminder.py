Task = input("Enter your task: ")

priority = int(input("Priority ('High', 'Medium', 'Low') : "))


Time_Bound = input("Is it time-bound? (yes/no): ").strip().lower() == "yes"

match priority:
    case "High":
        if Time_Bound == "yes":
            print(
                "Reminder: 'Finish project report' is a high priority task that requires immediate attention today!"
            )
        else:
            print(
                "Reminder: 'Finish project report' is a high priority task. Please complete it as soon as possible."
            )

    case "Medium":
        if Time_Bound == "yes":
            print(
                "Reminder: 'Prepare presentation' is a medium priority task that needs to be done this week!"
            )
        else:
            print(
                "Reminder: 'Prepare presentation' is a medium priority task. Please complete it when you can."
            )
            
    case "Low":
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
