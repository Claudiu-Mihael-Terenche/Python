str1 = 'geeksforgeeks'

str2 = ''
for item in str1:
	if item not in str2:
		str2 = str2 + item
print(str2)
