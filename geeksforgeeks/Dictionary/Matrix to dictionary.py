list1 = [[5, 6, 7], [8, 3, 2], [8, 2, 1]]

res1 = {idx: val for idx, val in enumerate(list1, start=1)}

res2 = {idx + 1: list1[idx] for idx in range(len(list1))}

print('The constructed dictionary:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Convert Matrix to dictionary
# Using dictionary comprehension + enumerate()

# initializing list

list1 = [[5, 6, 7], [8, 3, 2], [8, 2, 1]]

# printing original list
# print("The original list is : " + str(test_list))

# enumerate used to perform assigning row number

res1 = {idx: val for idx, val in enumerate(list1, start=1)}

# print('The constructed dictionary:', res1)

# Python3 code to demonstrate working of
# Convert Matrix to dictionary
# Using dictionary comprehension + range()

# initializing list
# test_list = [[5, 6, 7], [8, 3, 2], [8, 2, 1]]

# printing original list
# print("The original list is : " + str(test_list))

# using dictionary comprehension for iteration

res2 = {idx + 1: list1[idx] for idx in range(len(list1))}

print('The constructed dictionary:\n', res1, '\n', res2)
'''
