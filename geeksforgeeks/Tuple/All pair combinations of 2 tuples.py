from itertools import chain, product

tup1 = (4, 5); tup2 = (7, 8)

res1 = list(chain(product(tup1, tup2), product(tup2, tup1)))

res2 = []
for a in tup1:
	for b in tup2:
		res2.append((a, b))
		res2.append((b, a))

res3 = [(a, b) for a in tup1 for b in tup2] + [(a, b) for a in tup2 for b in tup1]

print('All pair combinations of 2 tuples:\n', res1, '\n', res2, '\n', res3)

'''
# Python3 code to do all pair combinations of 2 tuples using chain() + product()
from itertools import chain, product

tup1 = (4, 5)
tup2 = (7, 8)

# printing original tuples
# print("The original tuple 1 : " + str(tuple1))
# print("The original tuple 2 : " + str(tuple2))

# all pair combinations of 2 tuples using chain() + product()

res1 = list(chain(product(tup1, tup2), product(tup2, tup1)))

# print('The filtered tuple:', res1)

# tup21 = (4, 5)
# tup22 = (7, 8)

res2 = []
for a in tup1:
	for b in tup2:
		res2.append((a, b)) # append a tuple of the two elements to the filtered list
		res2.append((b, a)) # append a tuple of the two elements in reverse order to the filtered list

# print(res2)

# Using list comprehension

# tup31 = (4, 5)
# tup32 = (7, 8)

# printing original tuples
# print("The original tuple 1 : " + str(tup31))
# print("The original tuple 2 : " + str(tup32))

# generating all pair combinations of 2 tuples using list comprehension

res3 = [(a, b) for a in tup1 for b in tup2] + [(a, b) for a in tup2 for b in tup1]

print('All pair combinations of 2 tuples:\n', res1, '\n', res2, '\n', res3)
'''
