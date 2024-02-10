"""import math

a = int(input("Input the length of the pentagon's side: "))

area = 1 / 4 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * a ** 2

print('The area of your pentagon is ', area)"""

import math


def pentagon_area():
    # Input the number of sides
    n = int(input("Input the number of sides: "))

    # Check if the input is a pentagon
    if n != 5:
        print("A pentagon has 5 sides. Please enter a valid number of sides.")
        return

    # Input the side length
    s = float(input("Input the side length: "))

    # Calculate the area of the pentagon
    area = (1 / 4 * n * s ** 2) / math.tan(math.pi / n)

    # Print the result
    print(f"The area of the pentagon is {area}")


# Call the method
pentagon_area()
