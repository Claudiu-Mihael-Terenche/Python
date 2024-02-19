from operator import iand
tup1 = (10, 4, 6, 9)
tup2 = (5, 2, 3, 3)

res1 = tuple(map(iand, tup1, tup2))

res2 = tuple(tup1[i] & tup2[i] for i in range(len(tup1)))

res3 = tuple(ele1 & ele2 for ele1, ele2 in zip(tup1, tup2))

print('The AND tuple:\n', res1, '\n', res2, '\n', res3)

'''
# Python3 code to demonstrate working of
# Elementwise AND in tuples
# using map() + iand
from operator import iand

tup1 = (10, 4, 6, 9)
tup2 = (5, 2, 3, 3)

# printing original tuples
# print("The original tuple 1 : " + str(test_tup1))
# print("The original tuple 2 : " + str(test_tup2))

# Elementwise AND in tuples
# using map() + iand

res1 = tuple(map(iand, tup1, tup2))

# print('The AND tuple:', res1)

# Using a list comprehension and bitwise operators
# Initialize input tuples
# test_tup1 = (10, 4, 6, 9)
# test_tup2 = (5, 2, 3, 3)

# Perform elementwise AND operation using a list comprehension and bitwise &

res2 = tuple(tup1[i] & tup2[i] for i in range(len(tup1)))

# print('The AND tuple:', res2)

# Python3 code to demonstrate working of
# Elementwise AND in tuples
# using zip() + generator expression

# initialize tuples
# test_tup1 = (10, 4, 6, 9)
# test_tup2 = (5, 2, 3, 3)

# printing original tuples
# print("The original tuple 1 : " + str(test_tup1))
# print("The original tuple 2 : " + str(test_tup2))

# Elementwise AND in tuples
# using zip() + generator expression

res3 = tuple(ele1 & ele2 for ele1, ele2 in zip(tup1, tup2))

print('The AND tuple:\n', res1, '\n', res2, '\n', res3)
'''
