try:
    # Ask the user to enter a number
    print(abs(float(input("Enter a number: "))))

except ValueError:
    # Handle the case where the input is not a valid number
    print("Invalid input. Please enter a valid number.")
