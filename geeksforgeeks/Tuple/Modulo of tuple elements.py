from operator import mod
tup1 = (10, 4, 5, 6)
tup2 = (5, 6, 7, 5)

res1 = tuple(map(mod, tup1, tup2))

res2 = tuple(ele1 % ele2 for ele1, ele2 in zip(tup1, tup2))

print('The modulus tuple:\n', res1, '\n', res2)

'''
# Python3 code to create tuple modulo using map() + mod
from operator import mod

tup1 = (10, 4, 5, 6)
tup2 = (5, 6, 7, 5)

# printing original tuples
# print("The original tuple 1 : " + str(tup1))
# print("The original tuple 2 : " + str(tup2))

# tuple modulo using map() + mod

res1 = tuple(map(mod, tup1, tup2))

# print('The modulus tuple:', res1)

# Python3 code to create tuple modulo using zip() + generator expression

# tup21 = (10, 4, 5, 6)
# tup22 = (5, 6, 7, 5)

# Printing original tuples
# print("The original tuple 1 : " + str(tup21))
# print("The original tuple 2 : " + str(tup22))

# tuple modulo using zip() + generator expression

res2 = tuple(ele1 % ele2 for ele1, ele2 in zip(tup1, tup2))

print('The modulus tuple:\n', res1, '\n', res2)
'''
