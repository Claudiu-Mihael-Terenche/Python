from operator import xor

tup1 = (10, 4, 6, 9)
tup2 = (5, 2, 3, 3)

res1 = tuple(map(xor, tup1, tup2))

res2 = tuple(ele1 ^ ele2 for ele1, ele2 in zip(tup1, tup2))

res3 = tuple(tup1[item] ^ tup2[item] for item in range(len(tup1)))

print('The XOR tuple:\n', res1, '\n', res2, '\n', res3)

'''
# Python3 code to demonstrate working of
# Tuple XOR operation
# using map() + xor
from operator import xor

tup1 = (10, 4, 6, 9)
tup2 = (5, 2, 3, 3)

# printing original tuples
# print("The original tuple 1 : " + str(test_tup1))
# print("The original tuple 2 : " + str(test_tup2))

# Tuple XOR operation
# using map() + xor

res1 = tuple(map(xor, tup1, tup2))

# print('The XOR tuple:', res1)

# Python3 code to demonstrate working of
# Tuple XOR operation
# using zip() + generator expression

# test_tup1 = (10, 4, 6, 9)
# test_tup2 = (5, 2, 3, 3)

# printing original tuples
# print("The original tuple 1 : " + str(test_tup1))
# print("The original tuple 2 : " + str(test_tup2))

# Tuple XOR operation
# using zip() + generator expression

res2 = tuple(ele1 ^ ele2 for ele1, ele2 in zip(tup1, tup2))

# print('The XOR tuple:', res2)

# Using List Comprehension

# test_tup1 = (10, 4, 6, 9)
# test_tup2 = (5, 2, 3, 3)

# perform XOR operation using list comprehension

res3 = tuple(tup1[item] ^ tup2[item] for item in range(len(tup1)))

# printing original tuples
# print("The original tuple 1 : " + str(test_tup1))
# print("The original tuple 2 : " + str(test_tup2))

print('The XOR tuple:\n', res1, '\n', res2, '\n', res3)
'''
