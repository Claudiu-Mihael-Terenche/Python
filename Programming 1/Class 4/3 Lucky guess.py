import random

random_num = random.randint(1, 50)

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
age = int(input('Enter your age: '))
print(f'Hello {last_name}! You are {age} old. Nice to meet you!')

num = float(input('Please guess a number between 1 and 50: '))
if random_num == num:
    print('You are lucky!')
elif random_num < num:
    print('Choose a smaller number')
else:
    print('Choose a bigger number')
