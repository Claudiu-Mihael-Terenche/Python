def calculate_sum(a, b, c):
    return a + b + c

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    result = calculate_sum(num1, num2, num3)
    print("The sum of the numbers is:", result)

except ValueError:
    print("Invalid input. Please enter valid numbers.")

