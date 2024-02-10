def check_positive_negative(number):
    if number > 0:
        return 'positive'
    elif number < 0:
        return 'negative'
    else:
        return 'zero'

# Input from user
num = float(input('Enter a number: '))
result = check_positive_negative(num)
print(f'The number {num} is {result}.')
