import operator

tup1 = (10, 4, 5)
tup2 = (2, 5, 18)

res1 = tuple(map(operator.iand, tup1, tup2))

res2 = tuple(map(lambda i, j: i & j, tup1, tup2))

res3 = tuple(i & j for i, j in zip(tup1, tup2))

print('Resultant tuple after AND operation:\n', res1, '\n', res2, '\n', res3)

'''
# Python3 code to demonstrate working of
# Cross Tuple AND operation
# using map() + iand()
import operator

tup1 = (10, 4, 5)
tup2 = (2, 5, 18)

# printing original tuples
# print("The original tuple 1 : " + str(test_tup1))
# print("The original tuple 2 : " + str(test_tup2))

# Cross Tuple AND operation
# using map() + iand()

res1 = tuple(map(operator.iand, tup1, tup2))

# print('Resultant tuple after AND operation:', res1)

# Python3 code to demonstrate working of
# Cross Tuple AND operation
# using map() + lambda

# initialize tuples
# test_tup1 = (10, 4, 5)
# test_tup2 = (2, 5, 18)

# printing original tuples
# print("The original tuple 1 : " + str(test_tup1))
# print("The original tuple 2 : " + str(test_tup2))

# Cross Tuple AND operation
# using map() + lambda

res2 = tuple(map(lambda i, j: i & j, tup1, tup2))

# print('Resultant tuple after AND operation:', res2)

# Python3 code to demonstrate working of
# Cross Tuple AND operation
# using List comprehension

# initialize tuples
# test_tup1 = (10, 4, 5)
# test_tup2 = (2, 5, 18)

# printing original tuples
# print("The original tuple 1 : " + str(test_tup1))
# print("The original tuple 2 : " + str(test_tup2))

# Cross Tuple AND operation
# using List comprehension

res3 = tuple(i & j for i,j in zip(tup1, tup2))

print('Resultant tuple after AND operation:\n', res1, '\n', res2, '\n', res3)
'''
