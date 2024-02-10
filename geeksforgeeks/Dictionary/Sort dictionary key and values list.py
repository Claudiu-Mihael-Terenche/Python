dict1 = {'gfg': [7, 6, 3], 'is': [2, 10, 3], 'best': [19, 4]}

res1 = dict()
for key in sorted(dict1): res1[key] = sorted(dict1[key])

res2 = {key: sorted(dict1[key]) for key in sorted(dict1)}

print('The sorted dictionary:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Sort Dictionary key and values List
# Using loop + dictionary comprehension

dict1 = {'gfg': [7, 6, 3], 'is': [2, 10, 3], 'best': [19, 4]}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# Sort Dictionary key and values List
# Using loop + dictionary comprehension

res1 = dict()
for key in sorted(dict1): res1[key] = sorted(dict1[key])

# print('The sorted dictionary:', res1)

# Python3 code to demonstrate working of
# Sort Dictionary key and values List
# Using dictionary comprehension + sorted()

# initializing dictionary
# test_dict = {'gfg': [7, 6, 3], 'is': [2, 10, 3], 'best': [19, 4]}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# Sort Dictionary key and values List
# Using dictionary comprehension + sorted()

res2 = {key: sorted(dict1[key]) for key in sorted(dict1)}


print('The sorted dictionary:\n', res1, '\n', res2)
'''
