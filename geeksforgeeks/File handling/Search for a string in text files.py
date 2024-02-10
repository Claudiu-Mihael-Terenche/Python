word = input('Input the word to search: ')

with open(r'gfg input file.txt', 'r') as fp:
	lines = fp.readlines()
	for row in lines:
		if row.find(word) != -1:
			print('String exists in file')
			print('Line number:', lines.index(row))

with open(r'myfile.txt', 'r') as file:
	content = file.read()
	if word in content:
		print('String exist')
	else:
		print('String does not exist')

'''
# Using readline()
# string to search in file

# input1 = input('Input the word to search: ')
word1 = input('Input the word to search: ')

with open(r'gfg input file.txt', 'r') as fp:
	lines = fp.readlines() # read all lines using readline()
	for row in lines:
		# check if string present on a current line
		# word1 = input1
		# print(row.find(word))
		# find() method returns -1 if the value is not found,
		# if found it returns index of the first occurrence of the substring
		if row.find(word1) != -1:
			print('String exists in file')
			print('Line number:', lines.index(row))

# Using read()

word2 = input('Input the word to search: ')

with open(r'myfile.txt', 'r') as file:
	content = file.read() # read all content from a file using read()
	if word2 in content: # check if string present or not
		print('String exist')
	else:
		print('String does not exist')
'''
