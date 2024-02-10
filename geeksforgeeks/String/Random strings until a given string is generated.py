import string
import random
import time

possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'

str1 = 'Claudiu Mihael Terenche'

attemptThis = ''.join(random.choice(possibleCharacters)
                      for item in range(len(str1)))
attemptNext = ''

completed = False
iteration = 0

while completed == False:
    print(attemptThis)

    attemptNext = ''
    completed = True

    for item in range(len(str1)):
        if attemptThis[item] != str1[item]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += str1[item]

    iteration += 1
    attemptThis = attemptNext
    time.sleep(0.001)

print('Target matched after ' + str(iteration) + ' iterations')

'''
# Python program to generate and match the string from all random strings of same length

# importing string, random and time modules
import string
import random
import time

# all possible characters including lowercase, uppercase and special symbols
possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'

# string to be generated
str1 = 'Claudiu Mihael Terenche'

# to take input from user
# str1 = input(str('Enter your target text:'))

attemptThis = ''.join(random.choice(possibleCharacters)
                      for item in range(len(str1)))
attemptNext = ''

completed = False
iteration = 0

# iterate while completed is false
while completed == False:
    print(attemptThis)

    attemptNext = ''
    completed = True

    # fix the index if matches with the strings to be generated
    for item in range(len(str1)):
        if attemptThis[item] != str1[item]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += str1[item]

        # increment the iteration
    iteration += 1
    attemptThis = attemptNext
    time.sleep(0.001)

# driver Code
print('Target matched after ' + str(iteration) + ' iterations')
'''
