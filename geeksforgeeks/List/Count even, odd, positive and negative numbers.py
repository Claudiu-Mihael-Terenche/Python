list1 = [-10, 21, 4, -45, 66, 93, 11, 4.5, 'a', -4.5]

even_count1 = len([num for num in list1 if isinstance(num, int) and num % 2 == 0])
odd_count1 = len([num for num in list1 if isinstance(num, int) and num % 2 != 0])

pos_count1 = len([num for num in list1 if isinstance(num, int) and num > 0])
neg_count1 = len([num for num in list1 if isinstance(num, int) and num < 0])

even_count2, odd_count2 = 0, 0

for num in list1:
	if isinstance(num, int):
		if num % 2 == 0:
			even_count2 += 1
		else:
			odd_count2 += 1

pos_count2, neg_count2 = 0, 0

for num in list1:
	if isinstance(num, int):
		if num > 0:
			pos_count2 += 1
		elif num < 0:
			neg_count2 += 1

odd_count3 = len(list(filter(lambda num: isinstance(num, int) and num % 2 != 0, list1)))
even_count3 = len(list(filter(lambda num: isinstance(num, int) and num % 2 == 0, list1)))

pos_count3 = len(list(filter(lambda num: isinstance(num, int) and num > 0, list1)))
neg_count3 = len(list(filter(lambda num: isinstance(num, int) and num < 0, list1)))

print('Even nums:', even_count1, even_count2, even_count3, '\nOdd nums:', odd_count1, odd_count2, odd_count3)
print('Pos nums:', pos_count1, pos_count2, pos_count3, '\nNeg nums:', neg_count1, neg_count2, neg_count3)

'''
# Python program to print odd numbers in a list using list comprehension

list1 = [-10, 21, 4, -45, 66, 93, 11, 4.5, -4.5]

even_count1 = len([num for num in list1 if isinstance(num, int) if num % 2 == 0])
odd_count1 = len([num for num in list1 if isinstance(num, int) if num % 2 != 0])
pos_count1 = len([num for num in list1 if num > 0])
neg_count1 = len([num for num in list1 if num < 0])

# print('Even numbers in the list:', even_count1, '/ Odd numbers in the list:', odd_count1)

# Version 2: Python program to count even and odd numbers in a list using for loop

# list of numbers
# list2 = [10, 21, 4, 45, 66, 93, 11, 4.5]

even_count2, odd_count2 = 0, 0

for num in list1: # iterating each number in list
	if isinstance(num, int):
		if num % 2 == 0:
			even_count2 += 1
		else:
			odd_count2 += 1

pos_count2, neg_count2 = 0, 0

for num in list1: # iterating each number in list (see down 2 loops for printing without counting)
	if num > 0:
		pos_count2 += 1
	elif num < 0:
		neg_count2 += 1

# for ele_pos in list1:
	# if ele_pos > 0:
		# print(ele_pos)

# for ele_neg in list1:
	# if ele_neg < 0:
		# print(ele_neg)

# print('Even numbers in the list:', even_count2, '/ Odd numbers in the list:', odd_count2)

# Version 3: using lambda expressions
# list of numbers
# list3 = [10, 21, 4, 45, 66, 93, 11, 4.5]

odd_count3 = len(list(filter(lambda num: (num % 2 != 0 and isinstance(num, int)), list1)))
even_count3 = len(list(filter(lambda num: (num % 2 == 0 and isinstance(num, int)), list1)))
pos_count3 = len(list(filter(lambda num: (num > 0), list1)))
neg_count3 = len(list(filter(lambda num: (num < 0), list1)))

print('Even nums:', even_count1, even_count2, even_count3, '\nOdd nums:', odd_count1, odd_count2, odd_count3)
print('Pos nums:', pos_count1, pos_count2, pos_count3, '\nNeg nums:', neg_count1, neg_count2, neg_count3)
'''
