list1 = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]
cus_items = [6, 7, 8]

res1 = [[sub + (cus_items[idx], ) for sub in val] for idx, val in enumerate(list1)]

res2 = [[(idx, val) for idx in key] for key, val in zip(list1, cus_items)]

print('The matrix after row elements addition:\n', res1, '\n', res2)

'''
# Python3 code to do row-wise element addition in tuple matrix using enumerate() + list comprehension

list1 = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]

# printing original list
# print("The original list is : " + str(list2))

cus_items = [6, 7, 8]

# row-wise element addition in tuple matrix using enumerate() + list comprehension
res1 = [[sub + (cus_items[idx], ) for sub in val] for idx, val in enumerate(list1)]

# print('The matrix after row elements addition:', res1)

# Python3 code to do row-wise element addition in tuple matrix using zip() + list comprehension

# list1 = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]

# printing original list
# print("The original list is : " + str(list1))

# cus_items1 = [6, 7, 8]

# row-wise element addition in tuple matrix using zip() + list comprehension

res2 = [[(idx, val) for idx in key] for key, val in zip(list1, cus_items)]

print('The matrix after row elements addition:\n', res1, '\n', res2)
'''
