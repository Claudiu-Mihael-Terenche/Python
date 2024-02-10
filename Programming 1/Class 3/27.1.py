# Function to calculate salary
def calculate_salary(gender, years_of_service, qualifications):
    if gender == 'Male':
        if years_of_service >= 10:
            if qualifications == 'Post - Graduate':
                return 15000
            elif qualifications == 'Graduate':
                return 10000
        else:
            if qualifications == 'Post - Graduate':
                return 10000
            elif qualifications == 'Graduate':
                return 7000
    elif gender == 'Female':
        if years_of_service >= 10:
            if qualifications == 'Post - Graduate':
                return 12000
            elif qualifications == 'Graduate':
                return 9000
        else:
            if qualifications == 'Post - Graduate':
                return 10000
            elif qualifications == 'Graduate':
                return 6000

# Input data
gender = input("Enter gender (Male/Female): ")
years_of_service = int(input("Enter years of service: "))
qualifications = input("Enter qualifications (Graduate/Post - Graduate): ")

# Calculate and display salary
salary = calculate_salary(gender, years_of_service, qualifications)
if salary is not None:
    print("Salary:", salary)
else:
    print("Invalid input")
