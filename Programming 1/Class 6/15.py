def grade_description(grade):
    if grade == 'E':
        return 'Excellent'
    elif grade == 'V':
        return 'Very Good'
    elif grade == 'G':
        return 'Good'
    elif grade == 'A':
        return 'Average'
    elif grade == 'F':
        return 'Fail'
    else:
        return 'Invalid Grade'

# Accepting input from the user
user_grade = input("Enter the grade (E, V, G, A, F): ").upper()  # Convert to uppercase for case-insensitivity

# Displaying the equivalent description
description = grade_description(user_grade)
print(f"The equivalent description for grade {user_grade} is: {description}")
