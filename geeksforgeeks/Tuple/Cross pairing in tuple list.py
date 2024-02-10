list1 = [(1, 7), (6, 7), (9, 100), (4, 21)]; list2 = [(1, 3), (2, 1), (9, 7), (2, 17)]

res1 = [(a[1], b[1]) for a, b in zip(list1, list2) if a[0] == b[0]]

res2 = [(sub1[1], sub2[1]) for sub2 in list2 for sub1 in list1 if sub1[0] == sub2[0]]

print('The mapped tuples:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Cross Pairing in Tuple List
# Using zip() + list comprehension

list1 = [(1, 7), (6, 7), (9, 100), (4, 21)]
list2 = [(1, 3), (2, 1), (9, 7), (2, 17)]

# printing original lists
# print("The original list 1 : " + str(test_list1))
# print("The original list 2 : " + str(test_list2))

# zip() is used for pairing

res1 = [(a[1], b[1]) for a, b in zip(list1, list2) if a[0] == b[0]]

# print('The mapped tuples:', res1)

# Python3 code to demonstrate working of
# Cross Pairing in Tuple List
# Using list comprehension

# initializing lists
# test_list1 = [(1, 7), (6, 7), (9, 100), (4, 21)]
# test_list2 = [(1, 3), (2, 1), (9, 7), (2, 17)]

# printing original lists
# print("The original list 1 : " + str(test_list1))
# print("The original list 2 : " + str(test_list2))

# corresponding loop in list comprehension

res2 = [(sub1[1], sub2[1]) for sub2 in list2 for sub1 in list1 if sub1[0] == sub2[0]]

print('The mapped tuples:\n', res1, '\n', res2)
'''
