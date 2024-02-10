list1 = [(3, 4), (5, 6), (9, 10), (4, 5)]; list2 = [(5, 4), (3, 4), (6, 5), (9, 11)]

res1 = set(map(frozenset, list1)) & set(map(frozenset, list2))

res2 = []
for tup1 in list1:
	for tup2 in list2:
		if set(tup1) == set(tup2):
			res2.append(tup1)

res3 = list(set([tuple(sorted(ele)) for ele in list1]) & set([tuple(sorted(ele)) for ele in list2]))

set1 = set(frozenset(ele) for ele in list1)

set2 = set(frozenset(ele) for ele in list2)

res4 = [tuple(ele) for ele in (set1 & set2)]

print('List after intersection:\n', res1, '\n', res2, '\n', res3, '\n', res4)

'''
# Python3 code to demonstrate working of
# Tuple List intersection [ Order irrespective ]
# Using list comprehension + map() + frozenset() + & operator

list1 = [(3, 4), (5, 6), (9, 10), (4, 5)]
list2 = [(5, 4), (3, 4), (6, 5), (9, 11)]

# printing original list
# print("The original list 1 is : " + str(test_list1))
# print("The original list 2 is : " + str(test_list2))

# Using list comprehension + map() + frozenset() + & operator
# frozenset used as map() requires hashable container, which
# set is not, result in frozenset format

res1 = set(map(frozenset, list1)) & set(map(frozenset, list2))

# print('List after intersection:', res1)

# Using nested loops
# initializing lists
# test_list1 = [(3, 4), (5, 6), (9, 10), (4, 5)]
# test_list2 = [(5, 4), (3, 4), (6, 5), (9, 11)]

# Using nested loops

res2 = []
for tup1 in list1:
	for tup2 in list2:
		if set(tup1) == set(tup2):
			res2.append(tup1)

# print('List after intersection:', res2)

# Python3 code to demonstrate working of
# Tuple List intersection [ Order irrespective ]
# Using sorted() + set() + & operator + list comprehension

# initializing lists
# test_list1 = [(3, 4), (5, 6), (9, 10), (4, 5)]
# test_list2 = [(5, 4), (3, 4), (6, 5), (9, 11)]

# printing original list
# print("The original list 1 is : " + str(test_list1))
# print("The original list 2 is : " + str(test_list2))

# Using sorted() + set() + & operator + list comprehension
# Using & operator to intersect, sorting before performing intersection

res3 = list(set([tuple(sorted(ele)) for ele in list1]) & set([tuple(sorted(ele)) for ele in list2]))

# print('List after intersection:', res3)

# Python3 code to demonstrate working of
# Tuple List intersection [ Order irrespective ]
# Using set() + frozenset() + intersection() + list comprehension

# test_list1 = [(3, 4), (5, 6), (9, 10), (4, 5)]
# test_list2 = [(5, 4), (3, 4), (6, 5), (9, 11)]

# printing original list
# print("The original list 1 is : " + str(test_list1))
# print("The original list 2 is : " + str(test_list2))

# Using set() + frozenset() + intersection() + list comprehension

set1 = set(frozenset(ele) for ele in list1)

set2 = set(frozenset(ele) for ele in list2)

res4 = [tuple(ele) for ele in (set1 & set2)]

print('List after intersection:\n', res1, '\n', res2, '\n', res3, '\n', res4)
'''
