list1 = [1, 2, 5, 6]

res1 = [(val, pow(val, 3)) for val in list1]

res2 = [(val, val ** 3) for val in list1]

res3 = list(map(lambda val: (val, val ** 3), list1))

res4 = []
for val in list1:
	tup = (val, val ** 3)
	res4.append(tup)

print('\r', res1, '\n', res2, '\n', res3, '\n', res4)

'''
# Method #1 : Using pow() function.

list1 = [1, 2, 5, 6]

# using list comprehension to iterate each values in list and create a tuple as specified
res1 = [(val, pow(val, 3)) for val in list1]

# print(res1)

# Method #2: Using ** operator

# list2 = [1, 2, 5, 6]

# using list comprehension to iterate each values in list and create a tuple as specified

res2 = [(val, val ** 3) for val in list1]

# print(res2)

# Method #3: Using map() and lambda function
# list3 = [1, 2, 5, 6]

res3 = list(map(lambda val: (val, val ** 3), list1))

# print(res3)

# Method 4 : using a for loop to iterate through the values in the list
# and create a tuple of each value and its cube.

# creating a list

# list4 = [1, 2, 5, 6]

res4 = [] # creating an empty list to store the result
for val in list1:
	tup = (val, val ** 3) # creating a tuple of the value and its cube
	res4.append(tup) # adding the tuple to the result list

print('\r', res1, '\n', res2, '\n', res3, '\n', res4)
'''
