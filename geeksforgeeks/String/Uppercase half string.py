str1 = 'geeksforgeeks'

hlf_idx = len(str1) // 2

res1 = str1[:hlf_idx] + str1[hlf_idx:].upper()

res2 = ''
for idx in range(len(str1)):
	if idx >= hlf_idx:
		res2 += str1[idx].upper()
	else:
		res2 += str1[idx]

res3 = ''.join([str1[idx].upper() if idx >= hlf_idx else str1[idx] for idx in range(len(str1))])

print('The resultant string:\n', res1, '\n', res2, '\n', res3)

'''
# Python3 code to print uppercase half string using upper() + slicing string

# initializing string
str1 = 'geeksforgeeks'

# printing original string
# print('The original string is:', str(str1))

# computing half index
hlf_idx1 = len(str1) // 2

# Making new string with half upper case using slicing
# slicing takes one position less to ending position provided
res1 = str1[:hlf_idx1] + str1[hlf_idx1:].upper()

# printing result
print('The resultant string:', str(res1))

# Version 2: Python3 code to print uppercase half string using upper() + loop + len()

# initializing string
str2 = 'geeksforgeeks'

# printing original string
# print('The original string is :', str(str2))

# computing half index
hlf_idx2 = len(str2) // 2

res2 = ''
for idx2 in range(len(str2)):

	# uppercasing later half
	if idx2 >= hlf_idx2:
		res2 += str2[idx2].upper()
	else:
		res2 += str2[idx2]

# printing result
print('The resultant string:', str(res2))

# Version 3: Python3 code to print uppercase half string using list comprehension + join() + upper()

# initializing string
str3 = 'geeksforgeeks'

# printing original string
# print('The original string is:', str(str3))

# computing half index
hlf_idx3 = len(str3) // 2

# join() used to create result string
res3 = ''.join([str3[idx3].upper() if idx3 >= hlf_idx3 else str3[idx3]
			for idx3 in range(len(str3))])

# printing result
print('The resultant string:', str(res3))
'''
