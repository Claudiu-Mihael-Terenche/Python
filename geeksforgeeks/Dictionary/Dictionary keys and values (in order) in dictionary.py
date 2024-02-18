from itertools import chain
dict1 = {'Gfg': 1, 'is': 3, 'Best': 2}

keys = list(dict1.keys())
values = list(dict1.values())

res1 = keys + values

res2 = list(chain(keys, values))  # ???

print('The ordered keys and values:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Append Dictionary Keys and Values ( In order ) in dictionary
# Using values() + keys() + list()

# initializing dictionary

dict1 = {'Gfg': 1, 'is': 3, 'Best': 2}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# + operator is used to perform adding keys and values

res1 = list(dict1.keys()) + list(dict1.values())

# print('The ordered keys and values:', res1)

# Python3 code to demonstrate working of
# Append Dictionary Keys and Values ( In order ) in dictionary
# Using chain() + keys() + values()
from itertools import chain
# initializing dictionary
# test_dict = {"Gfg" : 1, "is" : 3, "Best" : 2}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# chain() is used for concatenation

res2 = list(chain(dict1.keys(), dict1.values()))

print('The ordered keys and values:\n', res1, '\n', res2)
'''
