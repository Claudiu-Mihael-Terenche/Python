import random

def generate_binary_string(n):

	number = random.getrandbits(n)

	binary_string = format(number, '0b')
	return binary_string


n = 7

print('Random binary string of length {}: {}'.format(n, generate_binary_string(n)))

def rand_key(p):

    key1 = ''
    for i in range(p):
        temp = str(random.randint(0, 1))
        key1 += temp
    return (key1)


str1 = rand_key(n)

print('Desired length random binary string is:', str1)

'''
# Using random.getrandbits():
import random

def generate_binary_string(n):
	# generate a random number with n bits
	number = random.getrandbits(n)
	# convert the number to binary
	binary_string = format(number, '0b')
	return binary_string

# test the function
n = 7
print('Random binary string of length {}: {}'.format(n, generate_binary_string(n)))

# Python program for random binary string generation
import random

# function to create the random binary string
def rand_key(p):
    # variable to store the string
    key1 = ''

    # loop to find the string of desired length
    for i in range(p):
        # randint function to generate 0, 1 randomly and converting the result into str
        temp = str(random.randint(0, 1))

        # concatenation the random 0, 1 to the final result
        key1 += temp

    return (key1)


# driver code
n = 7
str1 = rand_key(n)
print('Desired length random binary string is:', str1)
'''
