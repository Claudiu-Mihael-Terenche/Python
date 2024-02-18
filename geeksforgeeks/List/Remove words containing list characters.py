list1 = ['gfg', 'is', 'best', 'for', 'geeks']
char_list = ['g', 'o']

res = [item for item in list1 if all(ch not in item for ch in char_list)]

print('The filtered strings are:', res)

'''
# Python3 code to remove words containing list characters using list comprehension + all()
from itertools import groupby

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

char_list = ['g', 'o']

# printing original list
# print ('The original list is:', str(test_list))

# printing character list
# print ('The character list is:', str(char_list))

# remove words containing list characters using list comprehension + all()

res = [item for item in test_list if all(ch not in item for ch in char_list)]

print ('The filtered strings are:', res)
'''
