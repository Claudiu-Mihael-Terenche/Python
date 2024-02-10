# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Check if the numbers are in increasing order
if num1 < num2 < num3:
    print("The numbers are in increasing order.")
# Check if the numbers are in decreasing order
elif num1 > num2 > num3:
    print("The numbers are in decreasing order.")
# If neither increasing nor decreasing, they are in neither order
else:
    print("The numbers are in neither increasing nor decreasing order.")
