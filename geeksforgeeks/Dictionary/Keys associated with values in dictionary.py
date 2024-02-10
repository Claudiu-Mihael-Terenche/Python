from collections import defaultdict

dict1 = {'gfg': [1, 2, 3], 'is': [1, 4], 'best': [4, 2]}

res = defaultdict(list)
for key, val in dict1.items():
	for ele in val:
		res[ele].append(key)

print('The values associated dictionary:', dict(res))

'''
# Python3 code to demonstrate working of
# Values Associated Keys
# Using defaultdict() + loop
from collections import defaultdict

dict1 = {'gfg': [1, 2, 3], 'is': [1, 4], 'best': [4, 2]}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# Values Associated Keys
# Using defaultdict() + loop

res = defaultdict(list)
for key, val in dict1.items():
	for ele in val:
		res[ele].append(key)

print('The values associated dictionary:', dict(res))
'''
