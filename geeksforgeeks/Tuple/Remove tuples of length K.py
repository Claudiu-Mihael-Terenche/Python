list1 = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

K = 1

res1 = [ele for ele in list1 if len(ele) != K]

res2 = list(filter(lambda x : len(x) != K, list1))

print('Filtered list:\n', res1, '\n', res2)

'''
# Python3 code to remove tuples of length K using list comprehension

list1 = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

# printing original list
# print("The original list : " + str(list1))

K = 1

# 1 liner to perform task
# filter just lengths other than K
# len() used to compute length
res1 = [ele for ele in list1 if len(ele) != K]

# print('Filtered list:', res1)

# Python3 code to remove tuples of length K using filter() + lambda + len()

# list1 = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

# printing original list
# print("The original list : " + str(list1))

# K = 1

# filter() filters non K length values and returns result

res2 = list(filter(lambda x : len(x) != K, list1))

print('Filtered list:\n', res1, '\n', res2)
'''
