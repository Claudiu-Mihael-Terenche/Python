def calculate_gross_salary(basic_salary):
    if basic_salary < 1500:
        hra = 0.1 * basic_salary
        da_percentage = 90
    else:
        hra = 500
        da_percentage = 98

    da = (da_percentage / 100) * basic_salary

    gross_salary = basic_salary + hra + da
    return gross_salary


# Taking input for basic salary
basic_salary = float(input("Enter the basic salary: "))

# Calculate and print the gross salary
gross_salary = calculate_gross_salary(basic_salary)
print("Gross Salary:", gross_salary)
