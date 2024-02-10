alpha = 'abcdefghijklmnopqrstuvwxyz'
str1 = 'The quick brown fox jumps over the lazy dog'

str1 = str1.replace(' ','').lower()

str2 = ''.join(sorted(list(set(str1))))

res = str2 == alpha

print(res)

'''
# Using lower(),replace(),list(),set(),sort() and join() methods
# function to check if all elements are present or not

if (str2 == alpha):
	print('The string is a pangram')
else:
	print("The string isn't a pangram")
'''
