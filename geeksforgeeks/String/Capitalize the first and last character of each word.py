# Python program to capitalize first and last character of each word of a string
# using slicing and upper(),split() methods

str = 'welcome to geeksforgeeks'

word = str.split()

res = []
for item1 in word:
	item2 = item1[0].upper() + item1[1:-1] + item1[-1].upper()
	res.append(item2)

res = ' '.join(res)

print('String after:', res)
