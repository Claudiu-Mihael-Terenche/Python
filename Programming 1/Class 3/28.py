# Function to check if a string represents a positive number
def is_positive_number(value):
    try:
        num = float(value)
        return num > 0
    except ValueError:
        return False

# Get user input for hardness, carbon content, and tensile strength
hardness = input("Enter hardness: ")
carbon_content = input("Enter carbon content: ")
tensile_strength = input("Enter tensile strength: ")

# Check if the inputs are positive numbers
if not (is_positive_number(hardness) and is_positive_number(carbon_content) and is_positive_number(tensile_strength)):
    print("All inputs must be positive numbers.")
else:
    hardness = float(hardness)
    carbon_content = float(carbon_content)
    tensile_strength = float(tensile_strength)

    # Initialize the grade to 5 (none of the conditions met)
    grade = 5

    # Check the conditions and update the grade accordingly
    if hardness > 50:
        if carbon_content < 0.7:
            if tensile_strength > 5600:
                grade = 10  # All three conditions met
            else:
                grade = 7  # Conditions (i) and (iii) met
        else:
            grade = 9  # Conditions (i) and (ii) met
    elif carbon_content < 0.7:
        if tensile_strength > 5600:
            grade = 8  # Conditions (ii) and (iii) met
        else:
            grade = 6  # Only one condition met

    # Output the grade of the steel
    print(f"The grade of the steel is {grade}")
