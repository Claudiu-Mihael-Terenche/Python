list1 = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]

res1 = [sub for sub in list1 if all(ele >= 0 for ele in sub)]

res2 = list(filter(lambda sub: all(ele >= 0 for ele in sub), list1))

print('Positive elements tuples:\n', res1, '\n', res2)

'''
# Python3 code to find positive tuples in list using filter() + lambda + all()

list1 = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]

# printing original list
# print("The original list is : " + str(test_list))

# all() to check each element

res1 = list(filter(lambda sub: all(ele >= 0 for ele in sub), list1))

# print('Positive elements tuples:', res1)

# Python3 code to find positive tuples in list using list comprehension + all()

# test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]

# printing original list
# print("The original list is : " + str(test_list))

# all() to check each element

res2 = [sub for sub in list1 if all(ele >= 0 for ele in sub)]

print('Positive elements tuples:\n', res1, '\n', res2)
'''
