from collections import Counter

list1 = [1, 2, 2, 5, 8, 4, 4, 8]

res1 = len(set(list1))

res2 = len(Counter(list1).keys())

print('No of unique items in the list are:\n', res1, '\n', res2)

'''
list1 = [1, 2, 2, 5, 8, 4, 4, 8]

res1 = len(set(list1))

# print('No of unique items in the list are:', res1)

# Version 2
# importing Counter module

from collections import Counter

# list2 = [1, 2, 2, 5, 8, 4, 4, 8]

# creating a list with the keys

res2 = len(Counter(list1).keys())

print('No of unique items in the list are:', res1, res2)
'''
