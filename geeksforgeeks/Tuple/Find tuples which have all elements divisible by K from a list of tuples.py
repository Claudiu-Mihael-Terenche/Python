list1 = [(6, 24, 12), (7, 9, 6), (12, 18, 21)]
K = 6

res1 = [sub for sub in list1 if all(ele % K == 0 for ele in sub)]

res2 = list(filter(lambda sub: all(ele % K == 0 for ele in sub), list1))

print('K Multiple elements tuples:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# K Multiple Elements Tuples
# Using filter() + lambda + all()

list1 = [(6, 24, 12), (7, 9, 6), (12, 18, 21)]

# printing original list
# print("The original list is : " + str(list1))

K = 6

# filter() + lambda for filter operation
res1 = list(filter(lambda sub: all(ele % K == 0 for ele in sub), list1))

# print('K Multiple elements tuples:', res1)

# Python3 code to demonstrate working of
# K Multiple Elements Tuples
# Using list comprehension + all()

# initializing list
# test_list = [(6, 24, 12), (7, 9, 6), (12, 18, 21)]

# printing original list
# print("The original list is : " + str(test_list))

# initializing K
# K = 6

# all() used to filter elements

res2 = [sub for sub in list1 if all(ele % K == 0 for ele in sub)]

print('K Multiple elements tuples:\n', res1, '\n', res2)
'''
