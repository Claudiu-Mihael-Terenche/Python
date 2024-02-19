dict1 = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}
K = 6

res1 = {key: val for key, val in dict1.items() if not (isinstance(val, int) and (val > K))}

res2 = {}
for key in dict1:
    if not (isinstance(dict1[key], int) and dict1[key] > K):
        res2[key] = dict1[key]

res3 = dict(filter(lambda item: not (isinstance(item[1], int) and item[1] > K), dict1.items()))

print('The constructed dictionary:\n', res1, '\n', res2, '\n', res3)

'''
# Python3 code to demonstrate working of
# Remove keys with Values Greater than K ( Including mixed values )
# Using dictionary comprehension + isinstance()

# initializing dictionary

dict1 = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

K = 6

# using list comprehension to perform in one line
res1 = {key: val for key, val in dict1.items() if not (isinstance(val, int) and (val > K))}

# print('The constructed dictionary:', res1)

# Python3 code to demonstrate working of
# Remove keys with Values Greater than K ( Including mixed values )
# Using loop + isinstance()

# initializing dictionary
# test_dict = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# initializing K
# K = 6

# using loop to iterate keys of dictionary

res2 = {}
for key in dict1:
    if not (isinstance(dict1[key], int) and dict1[key] > K): # testing for data type and then condition,
        res2[key] = dict1[key] # order is imp.

# print('The constructed dictionary:', res2)

# Using dictionary comprehension and filter()
# initializing dictionary
# test_dict = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}

# printing original dictionary
# print("The original dictionary is: " + str(test_dict))

# initializing K
# K = 6

# using filter() and dictionary comprehension to construct a new dictionary

res3 = dict(filter(lambda item: not (isinstance(item[1], int) and item[1] > K), dict1.items()))

print('The constructed dictionary:\n', res1, '\n', res2, '\n', res3)
'''
