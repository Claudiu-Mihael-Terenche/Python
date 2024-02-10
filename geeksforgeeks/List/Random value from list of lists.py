from itertools import chain
import random

list1 = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

random_num = [0, 1, 2]

res1 = random.choice(list1[random.choice(random_num)])

res2 = random.choice(list(chain.from_iterable(list1)))

print('Random number from matrix:\n', res1, '\n', res2)

'''
# Python3 code for random matrix element using random.choice() [if row number given]
import random

list1 = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

# printing original list
# print('The original list is:', str(list1))

# initializing row number

random_num = [0, 1, 2]

# choice() for random number, from_iterables for flattening
res1 = random.choice(list1[random.choice(random_num)])

# printing result
# print('Random number from matrix row:', res1)

# Version 2: Python3 code for random matrix element using chain.from_iterables() + random.choice()
from itertools import chain
import random
# initializing list
# list2 = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

# printing original list
# print("The original list is : " + str(list2))

# choice() for random number, from_iterables for flattening

res2 = random.choice(list(chain.from_iterable(list1)))

print('Random number from matrix:\n', res1, '\n', res2)
'''
