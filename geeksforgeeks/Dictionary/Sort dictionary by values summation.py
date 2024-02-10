from collections import defaultdict

dict1 = {'Gfg': [6, 7, 4], 'is': [4, 3, 2], 'best': [7, 6, 5]}

temp1 = defaultdict(int)

for key, val in dict1.items(): temp1[key] = sum(val)

res1 = dict(sorted(temp1.items(), key=lambda x: x[1]))

temp2 = {key: sum(map(lambda ele: ele, dict1[key])) for key in dict1}

res2 = {key: temp2[key] for key in sorted(temp2, key=temp2.get)}

temp31 = {val: sum(int(idx) for idx in key) for val, key in dict1.items()}

temp32 = sorted(temp31.items(), key=lambda ele: temp31[ele[0]])

res3 = {key: val for key, val in temp32}

print('The sorted dictionary:\n', res1, '\n', res2, '\n', res3)

'''
# Using defaultdict() from the collections module
from collections import defaultdict

dict1 = {'Gfg': [6, 7, 4], 'is': [4, 3, 2], 'best': [7, 6, 5]}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# using defaultdict() to sum the values

temp1 = defaultdict(int)

for key, val in dict1.items(): temp1[key] = sum(val)

res1 = dict(sorted(temp1.items(), key=lambda x: x[1])) # sorting the dictionary based on the summed values

# print('The sorted dictionary:', res1)

# Python3 code to demonstrate working of
# Sort Dictionary by Values Summation
# Using map() + dictionary comprehension + sorted() + sum()

# initializing dictionary
# test_dict = {'Gfg' : [6, 7, 4], 'is' : [4, 3, 2], 'best' : [7, 6, 5]}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# summing all the values using sum()
# map() is used to extend summation to sorted()

temp2 = {key: sum(map(lambda ele: ele, dict1[key])) for key in dict1}

res2 = {key: temp2[key] for key in sorted(temp2, key=temp2.get)}

# print('The sorted dictionary:', res2)

# Python3 code to demonstrate working of
# Sort Dictionary by Values Summation
# Using dictionary comprehension + sum() + sorted()

# initializing dictionary
# test_dict = {'Gfg': [6, 7, 4], 'is': [4, 3, 2], 'best': [7, 6, 5]}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# summing all the values using sum()

temp31 = {val: sum(int(idx) for idx in key) for val, key in dict1.items()}

temp32 = sorted(temp31.items(), key=lambda ele: temp31[ele[0]]) # using sorted to perform sorting as required

res3 = {key: val for key, val in temp32} # rearrange into dictionary

print('The sorted dictionary:\n', res1, '\n', res2, '\n', res3)
'''
