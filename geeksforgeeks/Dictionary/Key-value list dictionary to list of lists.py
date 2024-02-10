dict1 = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

res1 = [[key] + dict1[key] for key in dict1]

res2 = []
for key, val in dict1.items():
	res2.append([key] + val)

res3 = [[key] + val for key, val in dict1.items()]

temp1 = list(dict1.keys())

res4 = list(map(lambda i: [i] + dict1[i], temp1))

print('The converted list is:\n', res1, '\n', res2, '\n', res3, '\n', res4)

'''
# Using a nested list comprehension
# initializing Dictionary

dict1 = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# Convert Key-Value list Dictionary to Lists of List
# Using a nested list comprehension

res1 = [[key] + dict1[key] for key in dict1]

# print('The converted list is:', res1)

# Python3 code to demonstrate working of
# Convert Key-Value list Dictionary to Lists of List
# Using loop + items()

# initializing Dictionary
# test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# Convert Key-Value list Dictionary to Lists of List
# Using loop + items()

res2 = []
for key, val in dict1.items():
	res2.append([key] + val)

# print('The converted list is:', res2)

# Python3 code to demonstrate working of
# Convert Key-Value list Dictionary to Lists of List
# Using list comprehension

# initializing Dictionary
# test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# Convert Key-Value list Dictionary to Lists of List
# Using list comprehension

res3 = [[key] + val for key, val in dict1.items()]

# print('The converted list is:', res3)

# Python3 code to demonstrate working of
# Convert Key-Value list Dictionary to Lists of List
# Using map + keys()

# initializing Dictionary
# test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

temp1 = list(dict1.keys())

# Convert Key-Value list Dictionary to Lists of List
# Using map + keys()

res4 = list(map(lambda i: [i] + dict1[i], temp1))

print('The converted list is:\n', res1, '\n', res2, '\n', res3, '\n', res4)
'''
