dict1 = {'Gfg': 4, 'is': 5, 'best': 9}
list1 = [8, 3, 2]

res1 = {}
for key, ele in zip(list1, dict1.items()):
    res1[key] = dict([ele])

res2 = {idx: {key: dict1[key]} for idx, key in zip(list1, dict1)}

print('The mapped dictionary:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Nested Dictionary with List
# Using loop + zip()

dict1 = {'Gfg': 4, 'is': 5, 'best': 9}
list1 = [8, 3, 2]

# printing original dictionary and list
# print("The original dictionary is : " + str(test_dict))
# print("The original list is : " + str(test_list))

# using zip() and loop to perform
# combining and assignment respectively.

res1 = {}
for key, ele in zip(list1, dict1.items()): res1[key] = dict([ele])

# print('The mapped dictionary:', res1)

# Python3 code to demonstrate working of
# Nested Dictionary with List
# Using dictionary comprehension + zip()

# initializing dictionary and list

# test_dict = {'Gfg': 4, 'is': 5, 'best': 9}
# test_list = [8, 3, 2]

# printing original dictionary and list
# print("The original dictionary is : " + str(test_dict))
# print("The original list is : " + str(test_list))

# zip() and dictionary comprehension mapped in one liner to solve

res2 = {idx: {key: dict1[key]} for idx, key in zip(list1, dict1)}

print('The mapped dictionary:\n', res1, '\n', res2)
'''
