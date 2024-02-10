# Using set

input = 'the big dwarf only jumps'

alphabets = [ch for ch in input if (ord('a') <= ord(ch) <= ord('z'))]

res = len(set(alphabets)) == len(alphabets)

print(res)

'''
# function to check whether a given string is heterogram or not
def heterogram(input):
	# separate out list of alphabets using list comprehension
	# ord function returns ascii value of character
	alphabets = [ch for ch in input if (ord('a') <= ord(ch) <= ord('z'))]
	# convert list of alphabets into set and compare lengths
	if len(set(alphabets)) == len(alphabets):
		print('Yes')
	else:
		print('No')


if __name__ == '__main__':
	input = 'the big dwarf only jumps'
	heterogram(input)
'''