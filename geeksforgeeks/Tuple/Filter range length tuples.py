list1 = [(4,), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]
i, j = 2, 3

res1 = [sub for sub in list1 if j >= len(sub) >= i]

res2 = list(filter(lambda ele: j >= len(ele) >= i, list1))

print('The tuple list after filtering range records:\n', res1, '\n', res2)

'''
# Python3 code to filter range length tuples using filter() + lambda + len()

list1 = [(4,), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]

# printing original list
# print("The original list is : " + str(list1))

i, j = 2, 3

# filter range length tuples using filter() + lambda + len()
res1 = list(filter(lambda ele: j >= len(ele) >= i, list1))

# print('The tuple list after filtering range records:', res1)

# Python3 code to filter range length tuples using list comprehension + len()

# list2 = [(4,), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]

# printing original list
# print("The original list is : " + str(list2))

# initializing desired lengths

# i2, j2 = 2, 3

# filter range length tuples using list comprehension + len()

res2 = [sub for sub in list1 if j >= len(sub) >= i]

print('The tuple list after filtering range records:\n', res1, '\n', res2)
'''
