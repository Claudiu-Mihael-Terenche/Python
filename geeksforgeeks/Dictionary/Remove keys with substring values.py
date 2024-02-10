dict1 = {1: 'Gfg is best for geeks', 2: 'Gfg is good', 3: 'I love Gfg'}

sub_list = ['love', 'good']

res1 = dict()
for key, val in dict1.items():
    if not any(ele in val for ele in sub_list):
        res1[key] = val

res2 = {key: val for key, val in dict1.items() if not any(ele in val for ele in sub_list)}

res3 = dict(filter(lambda item: not any(sub in item[1] for sub in sub_list), dict1.items()))

for key, value in list(dict1.items()):
	for sub in sub_list:
		if sub in value:
			dict1.pop(key)

print('Filtered dictionary:\n', res1, '\n', res2, '\n', res3, '\n', dict1)

'''
# Python3 code to demonstrate working of
# Remove keys with substring values
# Using any() + generator expression

# initializing dictionary

dict1 = {1: 'Gfg is best for geeks', 2: 'Gfg is good', 3: 'I love Gfg'}

# printing original dictionary
# print("The original dictionary : " + str(test_dict))

# initializing substrings

sub_list = ['love', 'good']

# Remove keys with substring values
# Using any() + generator expression

res1 = dict()
for key, val in dict1.items():
    if not any(ele in val for ele in sub_list):
        res1[key] = val

# print('Filtered dictionary:', res1)

# Python3 code to demonstrate working of
# Remove keys with substring values
# Using dictionary comprehension + any()

# initializing dictionary
# test_dict = {1: 'Gfg is best for geeks', 2: 'Gfg is good', 3: 'I love Gfg'}

# printing original dictionary
# print("The original dictionary : " + str(test_dict))

# initializing substrings
# sub_list = ['love', 'good']

# Remove keys with substring values
# Using dictionary comprehension + any()

res2 = {key: val for key, val in dict1.items() if not any(ele in val for ele in sub_list)}

# print('Filtered dictionary:', res2)

# Python3 code to demonstrate working of
# Remove keys with substring values
# Using filter() + lambda

# initializing dictionary
# test_dict = {1 : 'Gfg is best for geeks', 2 : 'Gfg is good', 3 : 'I love Gfg'}

# printing original dictionary
# print("The original dictionary : " + str(test_dict))

# initializing substrings
# sub_list = ['love', 'good']

# Remove keys with substring values
# Using filter() + lambda

res3 = dict(filter(lambda item: not any(sub in item[1] for sub in sub_list), dict1.items()))

# Using pop method
# test_dict = {1: 'Gfg is love', 2: 'Gfg is good'}
# sub_list = ['love', 'good']

for key, value in list(dict1.items()):
	for sub in sub_list:
		if sub in value:
			dict1.pop(key)

print('Filtered dictionary:\n', res1, '\n', res2, '\n', res3, '\n', dict1)
'''
