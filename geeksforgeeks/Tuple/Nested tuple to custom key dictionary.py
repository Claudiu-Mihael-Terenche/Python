tup = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))

keys = ['key', 'value', 'id']

res1 = [{key: val for key, val in zip(keys, sub)} for sub in tup]

res2 = [{'key': sub[0], 'value': sub[1], 'id': sub[2]} for sub in tup]

print('The converted dictionary:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Convert Nested Tuple to Custom Key Dictionary
# Using zip() + list comprehension

tup = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))

# printing original tuple
# print("The original tuple : " + str(test_tuple))

keys = ['key', 'value', 'id']

# Convert Nested Tuple to Custom Key Dictionary
# Using zip() + list comprehension

res1 = [{key: val for key, val in zip(keys, sub)} for sub in tup]

# print('The converted dictionary:', res1)

# Python3 code to demonstrate working of
# Convert Nested Tuple to Custom Key Dictionary
# Using list comprehension + dictionary comprehension

# initializing tuple
# test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))

# printing original tuple
# print("The original tuple : " + str(test_tuple))

# Convert Nested Tuple to Custom Key Dictionary
# Using list comprehension + dictionary comprehension

res2 = [{'key': sub[0], 'value': sub[1], 'id': sub[2]} for sub in tup]

print('The converted dictionary:\n', res1, '\n', res2)
'''
