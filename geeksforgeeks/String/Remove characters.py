# Using string.translate()

str1 = 'Geeks123For123Geeks'

res1 = str1.translate({ord(item): None for item in '123'})

print(res1)

'''
# Version 2: using string.replace()

# Removing 1st occurrence of s, i.e 5th pos.
res2 = str1.replace('123', '', 2)

# Printing string after removal of the first occurrences of s
print("The string after removal of i'th character:", res2)

# Version 3: Python3 program for removing i-th indexed character from a string

# removes character at index item


def remove(str3, item3):

	# characters before the i-th indexed is stored in a variable a
	a = str3[: item3]

	# characters after the nth indexed is stored in a variable b
	b = str3[item3 + 1:]

	# returning string after removing nth indexed character.
	return a + b


# driver code
if __name__ == '__main__':

	str3 = 'geeksFORgeeks'

	# remove nth index element
	item3 = 5

	# print the new string
	print(remove(str3, item3))

# Version 4: Python3 program for removing i-th indexed character from a string

# removes character at index item


def remove(str4, item4):
	if item4 > len(str4):
		return str4
	a = list(str4)
	a.pop(item4)
	return ''.join(a)


# driver code
if __name__ == '__main__':

	str4 = 'geeksFORgeeks'

	# remove nth index element
	item4 = 2

	# print the new string
	print(remove(str4, item4))
'''
