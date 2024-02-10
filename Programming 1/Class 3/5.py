def check_even_odd(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'

# Get input from user
num = float(input('Input your number '))

# Call the function and display the result
result = check_even_odd(num)
print(f'The number {num} is {result}.')