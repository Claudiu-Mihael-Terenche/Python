month = int(input('Enter a month (1 to 12): '))
year = int(input('Enter a year: '))

if 1 <= month <= 12:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month ==  10 or month == 12:
        print(f'The {month} month of the year {year} has 31 days')
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print(f'The {month} month of the year {year} has 30 days')
    elif (month % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f'The {month} month of the year {year} has 29 days')
    else:
        print(f'The {month} month of the year {year} has 28 days')
else:
    print('Input valid numbers')

"""def is_leap_year(year):
    # Leap year rules:
    # 1. If the year is divisible by 4
    # 2. If the year is not divisible by 100, except if it is divisible by 400
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    # List of days in each month (for non-leap years)
    days_in_month_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if it's a leap year and adjust February accordingly
    if is_leap_year(year):
        days_in_month_list[2] = 29

    # Validate the input
    if 1 <= month <= 12:
        return days_in_month_list[month]
    else:
        return None

# Get user input
try:
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year: "))

    # Calculate the number of days in the given month and year
    days = days_in_month(month, year)

    if days is not None:
        print(f"{month}/{year} had {days} days.")
    else:
        print("Invalid input. Month should be between 1 and 12.")
except ValueError:
    print("Invalid input. Please enter valid numbers for month and year.")"""
