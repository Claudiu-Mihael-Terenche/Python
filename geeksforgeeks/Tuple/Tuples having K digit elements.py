list1 = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]

K = 2

res1 = [sub for sub in list1 if all(len(str(ele)) == K for ele in sub)]

res2 = list(filter(lambda sub: all(len(str(ele)) == K for ele in sub), list1))

print('The extracted tuples:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Extract K digit Elements Tuples
# Using all() + list comprehension

list1 = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]

# printing original list
# print("The original list is : " + str(test_list))

K = 2

# using len() and str() to check length and perform string conversion
res1 = [sub for sub in list1 if all(len(str(ele)) == K for ele in sub)]

# print('The extracted tuples:', res1)

# Python3 code to demonstrate working of
# Extract K digit Elements Tuples
# Using all() + filter() + lambda

# list1 = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]

# printing original list
# print("The original list is : " + str(test_list))

# K = 2

# filter() and lambda used for task of filtering

res2 = list(filter(lambda sub: all(len(str(ele)) == K for ele in sub), list1))

print('The extracted tuples:\n', res1, '\n', res2)
'''
