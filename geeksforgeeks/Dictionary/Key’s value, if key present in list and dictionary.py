list1 = ['Gfg', 'is', 'Good', 'for', 'Geeks']
dict1 = {'Gfg': 2, 'is': 4, 'Best': 6}
K = 'Gfg'

res1 = None
if K in list1 and K in dict1:
	res1 = dict1.get(K)

res2 = None
if K in dict1.keys() and K in list1:
	res2 = dict1[K]

res3 = None
if K in set(list1).intersection(dict1):
	res3 = dict1[K]

res4 = None
for item in list1:
	if item == K:
		res4 = dict1.get(K)
		break

res5 = None
if all(K in sub for sub in [dict1, list1]):
	res5 = dict1[K]

print('Extracted value:\n', res1, '\n', res2, '\n', res3, '\n', res4, '\n', res5)

'''
# Python3 code to demonstrate working of
# Extract Key's Value, if Key Present in List and Dictionary
# Using any() + dictionary.get() method

# initializing list

list1 = ['Gfg', 'is', 'Good', 'for', 'Geeks']

dict1 = {'Gfg': 2, 'is': 4, 'Best': 6}

K = 'Gfg'

# printing original list and Dictionary
# print("The original list : " + str(test_list))
# print("The original Dictionary : " + str(test_dict))

# using any() to check for occurrence in list and dict
# accessing value of key using dictionary.get() method

res1 = None
if K in list1 and K in dict1: res1 = dict1.get(K)

# print('Extracted value:', res1)

# Python3 code to demonstrate working of
# Extract Key's Value, if Key Present in List and Dictionary

# initializing list
# test_list = ["Gfg", "is", "Good", "for", "Geeks"]

# initializing Dictionary
# test_dict = {"Gfg" : 2, "is" : 4, "Best" : 6}

# initializing K
# K = "Gfg"

# printing original list and Dictionary
# print("The original list : " + str(test_list))
# print("The original Dictionary : " + str(test_dict))

res2 = None
if K in dict1.keys() and K in list1: res2 = dict1[K]

# print('Extracted value:', res2)

# Python3 code to demonstrate working of
# Extract Key's Value, if Key Present in List and Dictionary
# Using set() + intersection()

# initializing list
# test_list = ["Gfg", "is", "Good", "for", "Geeks"]

# initializing Dictionary
# test_dict = {"Gfg" : 2, "is" : 4, "Best" : 6}

# initializing K
# K = "Gfg"

# printing original list and Dictionary
# print("The original list : " + str(test_list))
# print("The original Dictionary : " + str(test_dict))

# conversion of lists to set and intersection with keys
# using intersection

res3 = None
if K in set(list1).intersection(dict1): res3 = dict1[K]

# print('Extracted value:', res3)

# test_list = ["Gfg", "is", "Good", "for", "Geeks"]
# test_dict = {"Gfg" : 2, "is" : 4, "Best" : 6}
# K = "for"

# Method 9: Using a for loop to iterate through the list and dictionary

res4 = None
for item in list1:
	if item == K:
		res4 = dict1.get(K)
		break

# print('Extracted value:', res4)

# Python3 code to demonstrate working of
# Extract Key's Value, if Key Present in List and Dictionary
# Using all() + list comprehension

# initializing list
# test_list = ["Gfg", "is", "Good", "for", "Geeks"]

# initializing Dictionary
# test_dict = {"Gfg" : 2, "is" : 4, "Best" : 6}

# initializing K
# K = "Gfg"

# printing original list and Dictionary
# print("The original list : " + str(test_list))
# print("The original Dictionary : " + str(test_dict))

# using all() to check for occurrence in list and dict
# encapsulating list and dictionary keys in list

res5 = None
if all(K in sub for sub in [dict1, list1]): res5 = dict1[K]

print('Extracted value:\n', res1, '\n', res2, '\n', res3, '\n', res4, '\n', res5)
'''
