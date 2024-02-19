list1 = [[5, 8, 9], [2, 0, 9], [5, 4, 2], [2, 3, 9]]

res1 = dict(zip(list1[0], list1[1:]))

res2 = {list1[0][ele]: list1[ele + 1] for ele in range(len(list1) - 1)}

a = list1[0]

b = list1[1:len(list1)]

res3 = dict()
for i in range(0, len(a)):
    res3[a[i]] = b[i]

print('The assigned matrix:\n', res1, '\n', res2, '\n', res3)

'''
# Python3 code to demonstrate working of assigning Subsequent Rows to Matrix first row elements
# using zip() + list slicing + dict()

list1 = [[5, 8, 9], [2, 0, 9], [5, 4, 2], [2, 3, 9]]

# printing original list
# print("The original list : " + str(test_list))

# dict() to convert back to dict type
# slicing and pairing using zip() and list slicing

res1 = dict(zip(list1[0], list1[1:]))

# print('The assigned matrix:', res1)

# Python3 code to demonstrate working of
# Assigning Subsequent Rows to Matrix first row elements
# Using dictionary comprehension

# initializing list
# test_list = [[5, 8, 9], [2, 0, 9], [5, 4, 2], [2, 3, 9]]

# printing original list
# print("The original list : " + str(test_list))

# pairing each 1st col with next rows in Matrix

res2 = {list1[0][ele]: list1[ele + 1] for ele in range(len(list1) - 1)}

# print('The assigned matrix:', res2)

# Python3 code to demonstrate working of
# Assigning Subsequent Rows to Matrix first row elements
# Using for loop and slicing

# initializing list
# test_list = [[5, 8, 9], [2, 0, 9], [5, 4, 2], [2, 3, 9]]

# printing original list
# print("The original list : " + str(test_list))

# pairing each 1st col with next rows in Matrix

a = list1[0]

b = list1[1:len(list1)]

res3 = dict()
for i in range(0, len(a)): res3[a[i]] = b[i]

print('The assigned matrix:\n', res1, '\n', res2, '\n', res3)
'''
