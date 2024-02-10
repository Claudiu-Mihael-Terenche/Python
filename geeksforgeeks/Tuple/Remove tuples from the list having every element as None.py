list1 = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]

res1 = list(filter(lambda sub: not all(ele == None for ele in sub), list1))

res2 = [sub for sub in list1 if not all(ele == None for ele in sub)]

print('Removed None tuples:\n', res1, '\n', res2)

'''
# Python3 code to remove None tuples from list using filter() + lambda + all()

list1 = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]

# printing original list
# print("The original list is : " + str(list1))

# filter() + lambda to drive logic of discarding tuples

res1 = list(filter(lambda sub: not all(ele == None for ele in sub), list1))

# print('Removed None tuples:', res1)

# Python3 code to remove None tuples from list using all() + list comprehension

# list2 = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]

# printing original list
# print("The original list is : " + str(list2))

# negating result for discarding all None tuples

res2 = [sub for sub in list1 if not all(ele == None for ele in sub)]

print('Removed None tuples:\n', res1, '\n', res2)
'''
