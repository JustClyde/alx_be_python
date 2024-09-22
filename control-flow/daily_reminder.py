def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (super/high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Reminder message initialization
    reminder_message = f"'{task}' is a {priority} priority task."

    # Process the Task Based on Priority using Match Case
    match priority:
            case "super":
            reminder_message += " that requires immediate attention today!"
        case "high":
            reminder_message += " This task requires immediate attention today!"
        case "medium":
            reminder_message += " Please try to complete it today if possible."
        case "low":
            reminder_message += " Consider completing it when you have free time."
        case _:
            print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")
            return  # Exit the script if priority is invalid

    # Modifying the reminder if the task is time-bound
    if time_bound == "yes":
        if priority == "high":
            reminder_message = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder_message = f"'{task}' is a {priority} priority task, but it's time-bound. Please prioritize it."

    # Providing a customized reminder
    print(reminder_message)
