def get_weekday(week_number):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    if 1 <= week_number <= 8:
        return weekdays[week_number -1]
    else:
        return "Invalid week number"

try:
    week_number = int(input("Enter a week number (1-7): "))
    weekday = get_weekday(week_number)
    print(f"Weekday for week {week_number} is {weekday}")
except ValueError:
    print("Invalid input. Please enter a valid week number.")
