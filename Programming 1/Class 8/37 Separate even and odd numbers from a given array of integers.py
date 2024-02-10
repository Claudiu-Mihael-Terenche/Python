def separate_even_odd(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    result = even_numbers + odd_numbers
    return result

# Take user input for the array of integers
input_numbers = input("Enter a list of integers separated by spaces: ")
numbers = [int(num) for num in input_numbers.split()]

# Separate even and odd numbers
result_list = separate_even_odd(numbers)

# Display the result
print("Separated even and odd numbers:", result_list)
