list1 = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

res1 = dict()
for sub in list1:
	res1[tuple(sub[:2])] = tuple(sub[2:])

res2 = {tuple(sub[:2]): tuple(sub[2:]) for sub in list1}

res3 = {}
for sublist in list1:
	key = tuple(sublist[:2])
	value = tuple(sublist[2:])
	res3[key] = value

print('The mapped dictionary:\n', res1, '\n', res2, '\n', res3)

'''
# Using loop
# initializing list

list1 = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

# printing original list
# bprint("The original list is : " + str(test_list))

# Convert Lists of List to Dictionary
# Using loop

res1 = dict()
for sub in list1: res1[tuple(sub[:2])] = tuple(sub[2:])

# print('The mapped dictionary:', res1)

# Using dictionary comprehension
# initializing list
# test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

# printing original list
# print("The original list is : " + str(test_list))

# Convert Lists of List to Dictionary
# Using dictionary comprehension

res2 = {tuple(sub[:2]): tuple(sub[2:]) for sub in list1}

# print('The mapped dictionary:', res2)

# Using the zip() function and a loop
# initializing list
# test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

# printing original list
# print("The original list is : " + str(test_list))

# Convert Lists of List to Dictionary
# Using zip() and loop

res3 = {}
for sublist in list1:
	key = tuple(sublist[:2])
	value = tuple(sublist[2:])
	res3[key] = value

print('The mapped dictionary:\n', res1, '\n', res2, '\n', res3)
'''
