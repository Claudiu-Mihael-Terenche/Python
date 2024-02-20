# Using a list of tuples
dict1 = [
	('zero', '0'),
	('one', '1'),
	('two', '2'),
	('three', '3'),
	('four', '4'),
	('five', '5'),
	('six', '6'),
	('seven', '7'),
	('eight', '8'),
	('nine', '9')
]
str1 = 'zero four zero one'

# iterate over each word-digit pair and replacing the words with digits in the input string
for word, digit in dict1:
	str1 = str1.replace(word, digit)

# Method #2: Python3 code to convert numeric words to numbers using loop + join() + split()
dict2 = {
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9',
	'zero': '0'
}
str2 = 'zero four zero one'

res2 = ' '.join(dict2[item] for item in str2.split())

print('The string after performing replace:\n', str1, '\n', res2)
