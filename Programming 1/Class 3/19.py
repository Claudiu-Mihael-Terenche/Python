# Taking input for current year and year of joining
current_year = int(input("Enter the current year: "))
joining_year = int(input("Enter the year of joining: "))

# Calculating years of service
years_of_service = current_year - joining_year

# Checking if the employee is eligible for a bonus
if years_of_service > 3:
    bonus_amount = 2500
    print(f"Employee is eligible for a bonus of Rs. {bonus_amount}/-")
else:
    print("Employee is not eligible for a bonus.")
