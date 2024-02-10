list1 = [-10, -21, -4, 45, -66, 93]

pos_nos1 = [num for num in list1 if num > 0]
neg_nos1 = [num for num in list1 if num < 0]

print('Positive numbers:', *pos_nos1, '\nNegative numbers:', *neg_nos1)

for pos_nos2 in list1:
	if pos_nos2 > 0:
		print(pos_nos2, end=' ')

print('\r')

for neg_nos2 in list1:
	if neg_nos2 < 0:
		print(neg_nos2, end=' ')

'''
# Python program to print positive (negative) numbers in a list using list comprehension

# list of numbers

list1 = [-10, -21, -4, 45, -66, 93]

pos_nos1 = [num for num in list1 if num > 0] # using list comprehension
neg_nos1 = [num for num in list1 if num < 0]

print('Positive numbers:', *pos_nos1, '\nNegative numbers:', *neg_nos1)

# neg_nos and num < 0 for negative numbers

# Version 2: Python program to print positive (negative) numbers in a list using for loop

# list of numbers
# list2 = [11, -21, 0, 45, 66, -93]

# iterating each number in list

for pos_nos2 in list1:
	if pos_nos2 > 0: # checking condition
		print(pos_nos2, end=" ")

print('\r')

for neg_nos2 in list1:
	if neg_nos2 < 0: # checking condition
		print(neg_nos2, end=" ")
'''
