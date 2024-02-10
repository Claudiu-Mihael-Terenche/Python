# Python3 code to check if two strings are rotationally equivalent using loop + string slicing

str1 = 'geeks'; str2 = 'eksge'

res = False
for idx in range(len(str1)):
		if str1[idx: ] + str1[ :idx] == str2:
			res = True
			break

print('Are two strings Rotationally equal?', res)
