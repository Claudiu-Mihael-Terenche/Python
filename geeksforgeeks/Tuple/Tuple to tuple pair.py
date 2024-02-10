tup = (1, 2, 3, 4)

res1 = tuple(zip(tup[:-1], tup[1:]))

print(res1)

'''
# Using zip+ slicing

tup = (1, 2, 3, 4) # tup2 = ('G', 'F', 'G')

res1 = tuple(zip(tup[:-1], tup[1:]))

print(res1) # Output: ((1, 2), (2, 3), (3, 4))

# Python3 code to demonstrate working of
# Convert Tuple to Tuple Pair
# Using product() + next()

from itertools import product

tup2 = ('G', 'F', 'G')

# printing original tuple
# print("The original tuple : " + str(test_tuple))

# Convert Tuple to Tuple Pair
# Using product() + next()

tup2 = iter(tup2)

res2 = tuple(product(tup2, next(tup2)))

print('The paired records:', res2)
'''
