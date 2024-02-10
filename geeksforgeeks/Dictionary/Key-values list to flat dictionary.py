dict1 = {'month': [1, 2, 3], 'name': ['Jan', 'Feb', 'March']}

res1 = dict(zip(dict1['month'], dict1['name']))

res2 = {dict1['month'][i]: dict1['name'][i] for i in range(len(dict1['month']))}

res3 = {}
for i in range(len(dict1['month'])): res3[dict1['month'][i]] = dict1['name'][i]

print('Flattened dictionary:\n', res1, '\n', res2, '\n', res3)

'''
# Python3 code to demonstrate working of
# Convert key-values list to flat dictionary
# Using dict() + zip()

# initializing dictionary

dict1 = {'month': [1, 2, 3], 'name': ['Jan', 'Feb', 'March']}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# Convert key-values list to flat dictionary
# Using dict() + zip()

res1 = dict(zip(dict1['month'], dict1['name']))

# print('Flattened dictionary:', res1)

# Using a dictionary comprehension
# test_dict = {'month': [1, 2, 3], 'name': ['Jan', 'Feb', 'March']}

res2 = {dict1['month'][i]: dict1['name'][i] for i in range(len(dict1['month']))}

# print('Flattened dictionary:', res2)

# Python3 code to demonstrate working of
# Convert key-values list to flat dictionary
# Using for loop

# initializing dictionary
# test_dict = {'month' : [1, 2, 3], 'name' : ['Jan', 'Feb', 'March']}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# Convert key-values list to flat dictionary
# Using for loop

res3 = {}
for i in range(len(dict1['month'])): res3[dict1['month'][i]] = dict1['name'][i]

print('Flattened dictionary:\n', res1, '\n', res2, '\n', res3)
'''
