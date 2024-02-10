"""minutes = float(input('Input the number of minutes: '))

num_min_day = 24 * 60
num_min_year = 365 * num_min_day

years = minutes // num_min_year
rest_years = minutes % num_min_year

days = rest_years // num_min_day

print(f'This period of time is {years} years, {days} days long')"""

# Define constants for conversion
minutes_in_an_hour = 60
hours_in_a_day = 24
days_in_a_year = 365

# Input the number of minutes
minutes = int(input("Enter the number of minutes: "))

# Calculate the number of years and days
total_hours = minutes / minutes_in_an_hour
total_days = total_hours / hours_in_a_day
total_years = total_days / days_in_a_year

# Calculate the remaining days after removing full years
remaining_days = total_days % days_in_a_year

# Display the result
print(f"{minutes} minutes is approximately {int(total_years)} years and {int(remaining_days)} days.")
