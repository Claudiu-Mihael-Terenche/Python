# Input a five-digit number from the user
original_number = input("Enter a five-digit number: ")

# Check if the input is a valid five-digit number
if len(original_number) != 5 or not original_number.isdigit():
    print("Invalid input. Please enter a valid five-digit number.")
else:
    # Convert the input to an integer
    original_number = int(original_number)

    # Reverse the number
    reversed_number = 0
    temp = original_number
    while temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp = temp // 10

    # Check if the original and reversed numbers are equal
    if original_number == reversed_number:
        print(f"The original number ({original_number}) is equal to the reversed number ({reversed_number}).")
    else:
        print(f"The original number ({original_number}) is not equal to the reversed number ({reversed_number}).")

