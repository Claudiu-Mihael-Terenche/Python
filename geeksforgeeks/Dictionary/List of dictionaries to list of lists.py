list1 = [{'Nikhil' : 17, 'Akash' : 18, 'Akshat' : 20},
         {'Nikhil' : 21, 'Akash' : 30, 'Akshat' : 10},
         {'Nikhil' : 31, 'Akash' : 12, 'Akshat' : 19}]

res1 = [[key for key in list1[0].keys()], *[list(idx.values()) for idx in list1]]

res2 = []
for idx, sub in enumerate(list1, start=0):
	if idx == 0:
		res2.append(list(sub.keys()))
		res2.append(list(sub.values()))
	else:
		res2.append(list(sub.values()))

print('The converted list:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Convert List of Dictionaries to List of Lists
# Using list comprehension

# initializing list

list1 = [{'Nikhil' : 17, 'Akash' : 18, 'Akshat' : 20},
         {'Nikhil' : 21, 'Akash' : 30, 'Akshat' : 10},
         {'Nikhil' : 31, 'Akash' : 12, 'Akshat' : 19}]

# printing original list
# print("The original list is : " + str(test_list))

# Convert List of Dictionaries to List of Lists
# Using list comprehension

res1 = [[key for key in list1[0].keys()], *[list(idx.values()) for idx in list1]]

# print('The converted list:', res1)

# Using loop
# Using loop + enumerate()
# test_list = [{'Nikhil' : 17, 'Akash' : 18, 'Akshat' : 20},
			# {'Nikhil' : 21, 'Akash' : 30, 'Akshat' : 10},
			# {'Nikhil' : 31, 'Akash' : 12, 'Akshat' : 19}]

# printing original list
# print("The original list is : " + str(test_list))

# Convert List of Dictionaries to List of Lists
# Using loop + enumerate()

res2 = []
for idx, sub in enumerate(list1, start=0):
	if idx == 0:
		res2.append(list(sub.keys()))
		res2.append(list(sub.values()))
	else:
		res2.append(list(sub.values()))

print('The converted list:\n', res1, '\n', res2)
'''
