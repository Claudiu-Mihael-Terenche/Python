def extract_first_digit(number):
    # Convert the number to a string to easily access individual digits
    number_str = str(abs(num))

    # Return the first digit as an integer
    return int(number_str[0])

# Example usage:
num = int(input('Input your number: '))

first_digit = extract_first_digit(num)

print(f"First digit of {num}: {first_digit}")
