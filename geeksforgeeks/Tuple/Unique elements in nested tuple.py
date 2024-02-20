from itertools import chain
list1 = [(3, 4, 5), (4, 5, 7), (1, 4)]

res1 = list(set(chain.from_iterable(list1)))

res2 = sorted(set([item for inner in list1 for item in inner]))

print('Unique elements in nested tuples are:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Unique elements in nested tuple
# Using from_iterable() + set()
from itertools import chain

list1 = [(3, 4, 5), (4, 5, 7), (1, 4)]

# printing original list
# print("The original list : " + str(test_list))

# Unique elements in nested tuple
# Using from_iterable() + set()

res1 = list(set(chain.from_iterable(list1)))

# print('Unique elements in nested tuples are:', res1)

# Using a list comprehension and set conversion
# Python3 code to demonstrate working of
# Unique elements in nested tuple

# test_list = [(3, 4, 5), (4, 5, 7), (1, 4)]

# printing original list
# print("The original list : " + str(test_list))

# Unique elements in nested tuple
# Using list comprehension and set conversion

res2 = sorted(set([item for inner in list1 for item in inner]))

print('Unique elements in nested tuples are:\n', res1, '\n', res2)
'''
