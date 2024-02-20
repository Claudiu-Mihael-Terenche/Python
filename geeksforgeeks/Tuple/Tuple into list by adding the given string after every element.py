from itertools import chain
tup = (5, 6, 7, 4, 9)
K = 'Gfg'

res1 = list(chain.from_iterable((ele, K) for ele in tup))

res2 = [ele for sub in tup for ele in (sub, K)]

print('Converted tuple with K:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Convert tuple to List with succeeding element
# Using chain.from_iterable() + list() + generator expression
from itertools import chain

tup = (5, 6, 7, 4, 9)

# printing original tuple
# print("The original tuple is : ", test_tup)

K = 'Gfg'

# list comprehension for nested loop for flatten
res1 = list(chain.from_iterable((ele, K) for ele in tup))

# print('Converted tuple with K:', res1)

# Python3 code to demonstrate working of
# Convert tuple to List with succeeding element
# Using list comprehension

# test_tup = (5, 6, 7, 4, 9)

# printing original tuple
# print("The original tuple is : ", test_tup)

# K = "Gfg"

# list comprehension for nested loop for flatten

res2 = [ele for sub in tup for ele in (sub, K)]

print('Converted tuple with K:\n', res1, '\n', res2)
'''
