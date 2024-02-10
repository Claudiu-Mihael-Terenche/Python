from collections import Counter

# Using filter() method

str1 = 'geeksforgeeks'

x = filter(lambda x: str1.count(x) > 1, str1)

print(' '.join(set(x)))

'''
def find_dup_char(input):
	x = filter(lambda x: input.count(x) > 1, input)
	print(' '.join(set(x)))


if __name__ == '__main__':
	input = 'geeksforgeeks'
	find_dup_char(input)
'''

# Version 2: using Counter() method

def find_dup_char(input):

	# now create dictionary using counter method which will have strings as key and their frequencies as value
	WC = Counter(input)

	for letter, count in WC.items(): # finding no. of occurrence of a character and get the index of it
		if (count > 1):
			print(letter)


if __name__ == '__main__':
	input = 'geeksforgeeks'
	find_dup_char(input)

# Version 3: using count() method

def find_dup_char(input):
	x=[]
	for i in input:
		if i not in x and input.count(i) > 1:
			x.append(i)
	print(' '.join(x))


if __name__ == '__main__':
	input = 'geeksforgeeks'
	find_dup_char(input)
