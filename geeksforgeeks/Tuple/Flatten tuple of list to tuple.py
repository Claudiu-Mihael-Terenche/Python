from itertools import chain

tup = ([5, 6], [6, 7, 8, 9], [3])

res1 = tuple(chain(*tup))

res2 = tuple(sum(tup, []))

print('The flattened tuple:\n', res1, '\n', res2)

'''
from itertools import chain

tup = ([5, 6], [6, 7, 8, 9], [3])

# printing original tuple
# print("The original tuple : " + str(test_tuple))

# Flatten tuple of List to tuple
# Using itertools.chain() method

res1 = tuple(chain(*tup))

# print('The flattened tuple:', res1)

# Python3 code to demonstrate working of
# Flatten tuple of List to tuple
# Using sum() + tuple()

# tup = ([5, 6], [6, 7, 8, 9], [3])

# printing original tuple
# print("The original tuple : " + str(test_tuple))

# Flatten tuple of List to tuple
# Using sum() + tuple()

res2 = tuple(sum(tup, []))

print('The flattened tuple:\n', res1, '\n', res2)
'''
