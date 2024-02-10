dict1 = {'x': 10, 'y': 8}; dict2 = {'a': 6, 'b': 4}

dict31 = dict1 | dict2

dict32 = {**dict1, **dict2}

dict33 = dict1.copy()
dict33.update(dict2)

dict2.update(dict1)

print('\r', dict31, '\n', dict32, '\n', dict33, '\n', dict2)

'''
# Python code to merge dict using a single
# expression
# def Merge(dict1, dict2):
    # res = dict1 | dict2
    # return res


# Driver code
dict1 = {'x': 10, 'y': 8}; dict2 = {'a': 6, 'b': 4}

# dict3 = Merge(dict1, dict2)
#
dict31 = dict1 | dict2

# print(dict31)

# Python code to merge dict using a single
# expression
# def Merge(dict1, dict2):
    # res = {**dict1, **dict2}
    # return res


# Driver code
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
# dict3 = Merge(dict1, dict2)
dict32 = {**dict1, **dict2}

# print(dict32)

# def merge_dictionaries(dict1, dict2):
	# merged_dict = dict1.copy()
	# merged_dict.update(dict2)
	# return merged_dict

# Driver code
# dict1 = {'x': 10, 'y': 8}
# dict2 = {'a': 6, 'b': 4}

# print(merge_dictionaries(dict1, dict2))
dict33 = dict1.copy()
dict33.update(dict2)

# print(dict33)

# Python code to merge dict using update() method
# def Merge(dict1, dict2):
	# return(dict2.update(dict1))


# Driver code
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}

# This returns None
# print(Merge(dict1, dict2))

# changes made in dict2
# print(dict2)
dict2.update(dict1)

print('\r', dict31, '\n', dict32, '\n', dict33, '\n', dict2)
'''
