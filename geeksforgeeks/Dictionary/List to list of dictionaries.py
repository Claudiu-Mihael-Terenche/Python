import itertools

list1 = ['Gfg', 3, 'is', 8, 'Best', 10, 'for', 18, 'Geeks', 33]

key_list = ['name', 'number']

res1 = [{key_list[i]: val for i, val in enumerate(pair)} for pair in zip(list1[::2], list1[1::2])]

res2 = []
for pair in zip(list1[::2], list1[1::2]): res2.append({key_list[0]: pair[0], key_list[1]: pair[1]})

n = len(list1)
res3 = [{key_list[0]: list1[idx], key_list[1]: list1[idx + 1]} for idx in range(0, n, 2)]

print('The constructed dictionary list:\n', res1, '\n', res2, '\n', res3)

'''
# Using zip function and dictionary comprehension
# initializing lists

list1 = ['Gfg', 3, 'is', 8, 'Best', 10, 'for', 18, 'Geeks', 33]

key_list = ['name', 'number']

# using zip() function and dictionary comprehension
res1 = [{key_list[i]: val for i, val in enumerate(pair)} for pair in zip(list1[::2], list1[1::2])]

# print('The constructed dictionary list:', res1)

# Python3 code to demonstrate working of
# Convert List to List of dictionaries
# Using groupby() function from itertools module

# import itertools module
import itertools
# initializing lists
# test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]

# printing original list
# print("The original list : " + str(test_list))

# initializing key list
# key_list = ["name", "number"]

# using groupby() function to group elements into pairs

res2 = []
for pair in zip(list1[::2], list1[1::2]): res2.append({key_list[0]: pair[0], key_list[1]: pair[1]})

# print('The constructed dictionary list:', res2)

# Python3 code to demonstrate working of
# Convert List to List of dictionaries
# Using zip() + list comprehension

# initializing lists
# test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]

# printing original list
# print("The original list : " + str(test_list))

# initializing key list
# key_list = ["name", "number"]

# using list comprehension to perform as shorthand

n = len(list1)
res3 = [{key_list[0]: list1[idx], key_list[1]: list1[idx + 1]} for idx in range(0, n, 2)]

print('The constructed dictionary list:\n', res1, '\n', res2, '\n', res3)
'''
