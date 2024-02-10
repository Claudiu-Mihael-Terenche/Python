start = -4; end = 5

pos_nos1 = [num for num in range(start, end + 1) if num > 0]
neg_nos1 = [num for num in range(start, end + 1) if num < 0]

print('Positive numbers', *pos_nos1, '\nNegative numbers', *neg_nos1)

for pos_nos2 in range(start, end + 1):
	if pos_nos2 > 0:
		print(pos_nos2, end=' ')

print('\r')

for neg_nos2 in range(start, end + 1):
	if neg_nos2 < 0:
		print(neg_nos2, end=' ')

'''
# Python code to print all positive (negative) numbers in a given range using list comprehension

start = -4; end = 5

pos_nos1 = [num for num in range(start, end + 1) if num > 0]
neg_nos1 = [num for num in range(start, end + 1) if num < 0]

print('Positive numbers', *pos_nos1, '\nNegative numbers', *neg_nos1)

# i < 0 for negative numbers

# Version 2: Python program to print positive (negative) numbers in given range using for loop

# start, end = -4, 19

# iterating each number in list

for pos_nos2 in range(start, end + 1):
	if pos_nos2 > 0: # checking condition
		print(pos_nos2, end=' ')

print('\r')

for neg_nos2 in range(start, end + 1):
	if neg_nos2 < 0: # checking condition
		print(neg_nos2, end=' ')
'''
