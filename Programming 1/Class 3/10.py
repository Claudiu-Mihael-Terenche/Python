def is_valid_triangle(angle1, angle2, angle3):
    # Check if the sum of angles is 180 degrees
    if angle1 + angle2 + angle3 == 180:
        return True
    else:
        return False

# Input angles from the user
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

# Check if the triangle is valid
if is_valid_triangle(angle1, angle2, angle3):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
