list1 = [('GFg', 5, 9), ('is', 4, 3), ('best', 10, 29)]
check_list = [4, 2, 8, 10]
K = 1

res1 = [sub for sub in list1 if sub[K] in check_list]

res2 = []
for tup in list1:
	if tup[K] in check_list:
		res2.append(tup)

res3 = list(filter(lambda sub: sub[K] in check_list, list1))

print('The filtered tuples:\n', res1, '\n', res2, '\n', res3)

'''
# Python3 code to filter tuples by Kth element from list using list comprehension

list1 = [('GFg', 5, 9), ('is', 4, 3), ('best', 10, 29)]

# printing original list
# print("The original list is : " + str(test_list))

check_list = [4, 2, 8, 10]

K = 1

# checking for presence on Kth element in list one liner
res1 = [sub for sub in list1 if sub[K] in check_list]

# print('The filtered tuples:', res1)

# Python3 code to demonstrate working of
# Filter Tuples by Kth element from List
# Using for loop

# initializing list
# test_list = [("GFg", 5, 9), ("is", 4, 3), ("best", 10, 29)]

# printing original list
# print("The original list is : " + str(test_list))

# initializing check_list
# check_list = [4, 2, 8, 10]

# initializing K
# K = 1

# initializing empty result list

res2 = []
for tup in list1:
	if tup[K] in check_list: # checking if Kth element is in check_list
		res2.append(tup) # appending tuple to result list

# print('The filtered tuples:', res2)

# Python3 code to demonstrate working of
# Filter Tuples by Kth element from List
# Using filter() + lambda

# initializing list
# test_list = [("GFg", 5, 9), ("is", 4, 3), ("best", 10, 29)]

# printing original list
# print("The original list is : " + str(test_list))

# initializing check_list
# check_list = [4, 2, 8, 10]

# initializing K
# K = 1

# filter() perform filter, lambda func. checks for presence
# one liner

res3 = list(filter(lambda sub: sub[K] in check_list, list1))

print('The filtered tuples:\n', res1, '\n', res2, '\n', res3)
'''
