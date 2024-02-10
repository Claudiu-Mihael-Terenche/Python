list1 = [['Gfg', 'is', 'Best'], ['Gfg', 'is', 'love'], ['Gfg', 'is', 'for', 'Geeks']]

res1 = tuple(tuple(sub) for sub in list1)

res2 = tuple(map(tuple, list1))

print('The converted data:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Convert List of Lists to Tuple of Tuples
# using tuple + list comprehension

list1 = [['Gfg', 'is', 'Best'], ['Gfg', 'is', 'love'], ['Gfg', 'is', 'for', 'Geeks']]

# Printing original list
# print("The original list is : " + str(test_list))

# Convert List of Lists to Tuple of Tuples
# using tuple + list comprehension

res1 = tuple(tuple(sub) for sub in list1)

# print('The converted data:', res1)

# Python3 code to demonstrate working of
# Convert List of Lists to Tuple of Tuples
# Using map() + tuple()

# Initializing list
# test_list = [['Gfg', 'is', 'Best'], ['Gfg', 'is', 'love'], ['Gfg', 'is', 'for', 'Geeks']]

# Printing original list
# print("The original list is : " + str(test_list))

# Convert List of Lists to Tuple of Tuples
# using map() + tuple()

res2 = tuple(map(tuple, list1))

print('The converted data:\n', res1, '\n', res2)
'''
