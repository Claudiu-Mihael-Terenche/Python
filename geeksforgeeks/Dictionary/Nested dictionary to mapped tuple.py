from collections import defaultdict
dict1 = {'gfg': {'x': 5, 'y': 6}, 'is': {'x': 1, 'y': 4}, 'best': {'x': 8, 'y': 3}}

res = defaultdict(tuple)
for key, val in dict1.items():
	for ele in val:
		res[ele] += (val[ele], )

print('The grouped dictionary:', list(res.items()))

'''
# Python3 code to demonstrate working of
# Convert Nested dictionary to Mapped Tuple
# Using defaultdict() + loop
from collections import defaultdict

dict1 = {'gfg': {'x': 5, 'y': 6}, 'is': {'x': 1, 'y': 4}, 'best': {'x': 8, 'y': 3}}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# Convert Nested dictionary to Mapped Tuple
# Using defaultdict() + loop

res = defaultdict(tuple)
for key, val in dict1.items():
	for ele in val:
		res[ele] += (val[ele], )

print('The grouped dictionary:', list(res.items()))
'''
