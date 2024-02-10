str1 = 'geeks for geeks'

substr1 = 'geeks'

start = 0

end = 1000

print(str1.index('for', start, end))

res1 = ['yes' if substr1 in str1 else 'no']

print(*res1)

if 'for' in str1:
	print('Yes! It is present in the string')
else:
	print('No! It is not present')
