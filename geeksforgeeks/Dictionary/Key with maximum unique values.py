dict1 = {'Gfg': [5, 7, 5, 4, 5], 'is': [6, 7, 4, 3, 3], 'Best': [9, 9, 6, 5, 5]}

max_key = sorted(dict1, key=lambda ele: len(set(dict1[ele])), reverse=True)[0]

print('Key with maximum unique values:', max_key)

'''
# Python3 code to demonstrate working of
# Key with maximum unique values
# Using sorted() + lambda() + set() + values() + len()

# Initializing dictionary

dict = {'Gfg': [5, 7, 5, 4, 5], 'is': [6, 7, 4, 3, 3], 'Best': [9, 9, 6, 5, 5]}

# printing original dictionary
# print('The original dictionary is:', str(dict))

# sorting to reverse sort dictionary

max_key = sorted(dict, key=lambda ele: len(set(dict[ele])), reverse=True)[0]

print('Key with maximum unique values:', max_key)
'''
