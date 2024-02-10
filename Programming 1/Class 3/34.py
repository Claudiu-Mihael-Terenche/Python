# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Display the menu
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Input from the user
choice = input("Enter choice (1/2/3/4): ")

# Check if the input is valid
if choice not in ('1', '2', '3', '4'):
    print("Invalid input")
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result: ", add(num1, num2))
    elif choice == '2':
        print("Result: ", subtract(num1, num2))
    elif choice == '3':
        print("Result: ", multiply(num1, num2))
    elif choice == '4':
        print("Result: ", divide(num1, num2))
