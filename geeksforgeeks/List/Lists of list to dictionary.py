from functools import reduce
list1 = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

res1 = {tuple(sub[:2]): tuple(sub[2:]) for sub in list1}

res2 = dict()
for sub in list1:
    res2[tuple(sub[:2])] = tuple(sub[2:])


def combine_dicts(dict1, dict2):
    dict1.update(dict2)
    return dict1


res3 = reduce(combine_dicts, [{tuple(sub[:2]): tuple(sub[2:])} for sub in list1])

print('The mapped dictionary:\n', res1, '\n', res2, '\n', res3)

'''
# Python3 code to convert lists of list to dictionary using dictionary comprehension

# initializing list

list1 = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

# printing original list
# print("The original list is : " + str(list1))

# Convert lists of list to dictionary using dictionary comprehension

res1 = {tuple(sub[:2]): tuple(sub[2:]) for sub in list1}

# printing result
# print('The mapped dictionary:', str(res))

# Version 2: Python3 code to convert lists of list to dictionary using loop

# initializing list
# list2 = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

# printing original list
# print('The original list is:', str(list2))

# convert lists of list to dictionary using loop

res2 = dict()
for sub in list1:
    res2[tuple(sub[:2])] = tuple(sub[2:])

# printing result
# print('The mapped dictionary:', str(res))

# Version 3: using the reduce() function
from functools import reduce
# initializing list
# list3 = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

# printing original list
# print('The original list is:', str(list3))

# define function to combine dictionaries

def combine_dicts(dict1, dict2):
dict1.update(dict2)
return dict1

# use reduce to apply combine_dicts to all nested dictionaries
res3 = reduce(combine_dicts, [{tuple(sub[:2]): tuple(sub[2:])} for sub in list1])

print('The mapped dictionary:\n', res1, '\n', res2, '\n', res3) # print mapped dictionary
'''
