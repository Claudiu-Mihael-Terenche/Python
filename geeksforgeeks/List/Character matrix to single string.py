from itertools import chain
list1 = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]

res1 = ''.join(chain(*list1))

res2 = ''.join(item for sub in list1 for item in sub)

print('The string after join:\n', res1, '\n', res2)

'''
# Python3 code to convert character matrix to single string using join() + chain()
from itertools import chain

list1 = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]

# printing original list
# print('The original list is:', str(list1))

# convert character matrix to single string using join() + chain()

res1 = ''.join(chain(*list1))
res2 = ''.join(item for sub in list1 for item in sub)

print('The string after join:\n', res1, '\n', res2)

# Version 2: Python3 code to convert character matrix to single string using join() + list comprehension

# initializing list
# list2 = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]

# printing original list
# print('The original list is:', str(list2))

# convert character matrix to single string using join() + list comprehension
# res2 = ''.join(item for sub in list2 for item in sub)

# printing result
# print('The string after join:', res2)
'''
