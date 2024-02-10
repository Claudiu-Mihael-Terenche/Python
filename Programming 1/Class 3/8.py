def get_monthName(month_number):
    monthName = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    if 1 <= month_number <= 13:
        return monthName[month_number -1]
    else:
        return "Invalid month number"

try:
    month_number = int(input("Enter a month number (1-12): "))
    monthName = get_monthName(month_number)
    print(f"Month name for month {month_number} is {monthName}")
except ValueError:
    print("Invalid input. Please enter a valid month number.")
