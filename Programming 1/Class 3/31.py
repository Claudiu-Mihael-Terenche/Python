# Accept three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Check if all numbers are equal
if num1 == num2 and num2 == num3:
    print("All numbers are equal.")
else:
    print("Not all numbers are equal.")
