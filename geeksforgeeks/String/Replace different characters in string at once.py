# Python3 code to replace different characters in string at once using key() and replace() methods
str1 = 'geeksforgeeks is best'
map_dict = {'e': '1', 'b': '6', 'i': '4'}

for item in str1:
	if item in map_dict.keys():
		str1 = str1.replace(item, map_dict[item])

print('The converted string:', str1)
