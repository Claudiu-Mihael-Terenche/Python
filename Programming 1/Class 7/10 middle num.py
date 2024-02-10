def is_middle_point(a, b, c):
    # Sort the numbers in ascending order
    sorted_numbers = sorted([a, b, c])

    # Check if the middle number is equal to the average of the other two
    return sorted_numbers[1] == (sorted_numbers[0] + sorted_numbers[2]) / 2

# Example usage:
num1 = int(input('Input the first number: '))
num2 = int(input('Input the second number: '))
num3 = int(input('Input the third number: '))

result = is_middle_point(num1, num2, num3)
print(result)
