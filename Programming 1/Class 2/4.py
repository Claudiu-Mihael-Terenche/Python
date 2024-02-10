def calculate_average(a, b, c):
    return (a + b + c) / 3

try:
    num1 = float(input('Input the first number '))
    num2 = float(input('Input the second number '))
    num3 = float(input('Input the third number '))

    result = calculate_average(num1, num2, num3)
    print('The average number is: ', result)

except ValueError:
    print('Invalid input. Enter valid numbers')
