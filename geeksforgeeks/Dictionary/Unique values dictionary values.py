from itertools import chain
dict1 = {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}

res1 = list(set(sum(dict1.values(), [])))

res2 = list(sorted(set(chain(*dict1.values()))))

res3 = list(sorted({ele for val in dict1.values() for ele in val}))

print('The unique values list is:\n', res1, '\n', res2, '\n', res3)

'''
# Python3 code to demonstrate working of extract unique values dictionary values

dict1 = {'gfg' : [5, 6, 7, 8], 'is' : [10, 11, 7, 5], 'best' : [6, 12, 10, 8], 'for' : [1, 2, 5]}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# extract unique values dictionary values

res1 = list(set(sum(dict1.values(), [])))

# print('The unique values list is:', res1)

# Python3 code to demonstrate working of extract Unique values dictionary values
# using chain() + sorted() + values()
from itertools import chain

# test_dict = {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# Extract Unique values dictionary values using chain() + sorted() + values()

res2 = list(sorted(set(chain(*dict1.values()))))

# print('The unique values list is:', res2)

# Python3 code to demonstrate working of extract Unique values dictionary values
# using set comprehension + values() + sorted()

# dict1 = {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# Extract Unique values dictionary values using set comprehension + values() + sorted()

res3 = list(sorted({ele for val in dict1.values() for ele in val}))

print('The unique values list is:\n', res1, '\n', res2, '\n', res3)
'''
