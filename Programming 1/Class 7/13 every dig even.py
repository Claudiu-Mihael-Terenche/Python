def all_digits_even(number):
    # Convert the number to a string to iterate through its digits
    str_number = str(num)

    # Check if every digit is even
    for digit_str in str_number:
        digit = int(digit_str)
        if digit % 2 != 0:
            return False

    # If the loop completes without returning False, every digit is even
    return True

# Example usage:
num = int(input('Input your number: '))
result = all_digits_even(num)
print(result)  # Output: True or False
