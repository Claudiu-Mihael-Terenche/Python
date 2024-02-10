def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Found a factor, not a prime number

    return True  # If no factors found, it's a prime number

# Get input from the user
user_number = int(input("Enter a number: "))

# Check if the user-provided number is prime or not
if is_prime(user_number):
    print(f"{user_number} is a prime number.")
else:
    print(f"{user_number} is not a prime number.")
