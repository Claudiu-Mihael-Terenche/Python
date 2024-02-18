dict1 = {'Gfg': 4, 'is': 2, 'best': 3, 'for': 'geeks'}
K = 3

res1 = {key: val for key, val in dict1.items() if type(val) != int or val > K}  # ???

res2 = {key: val for key, val in dict1.items() if not isinstance(val, int) or val > K}

res3 = {}
for key, val in dict1.items():
    if type(val) != int or val > K:  # ???
        res3[key] = val

print('Values greater than K:\n', res1, '\n', res2, '\n', res3)

'''
# Python3 code to demonstrate working of
# Filter dictionary values in heterogeneous dictionary
# Using type() + dictionary comprehension

# initializing dictionary

dict1 = {'Gfg' : 4, 'is' : 2, 'best' : 3, 'for' : 'geeks'}

# printing original dictionary
# print("The original dictionary : " + str(test_dict))

# initializing K

K = 3

# Filter dictionary values in heterogeneous dictionary
# Using type() + dictionary comprehension

res1 = {key: val for key, val in dict1.items() if type(val) != int or val > K}

# print('Values greater than K:', str(res1))

# Python3 code to demonstrate working of
# Filter dictionary values in heterogeneous dictionary
# Using isinstance() + dictionary comprehension

# initializing dictionary
# test_dict = {'Gfg' : 4, 'is' : 2, 'best' : 3, 'for' : 'geeks'}

# printing original dictionary
# print("The original dictionary : " + str(test_dict))

# initializing K
# K = 3

# Filter dictionary values in heterogeneous dictionary
# Using isinstance() + dictionary comprehension

res2 = {key: val for key, val in dict1.items() if not isinstance(val, int) or val > K}

# print('Values greater than K:', str(res2))

# Python3 code to demonstrate working of
# Filter dictionary values in heterogeneous dictionary
# Using for loop and conditional statements

# initializing dictionary
# test_dict = {'Gfg' : 4, 'is' : 2, 'best' : 3, 'for' : 'geeks'}

# printing original dictionary
# print("The original dictionary : " + str(test_dict))

# initializing K
# K = 3

# Filter dictionary values in heterogeneous dictionary
# Using for loop and conditional statements

res3 = {}
for key, val in dict1.items():
if type(val) != int or val > K:
res3[key] = val

print('Values greater than K:\n', res1, '\n', res2, '\n', res3)
'''
