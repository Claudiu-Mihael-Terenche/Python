str1 = 'geeksforgeeks 33 is best'

str11 = str1.replace(' ','')

res1 = len(str11)

res2 = sum(not item.isspace() for item in str1)

res3 = len(''.join([item for item in str1 if item != ' ']))

str13 = str1.translate({ord(item): None for item in ' '})

res4 = len(str13)

res5 = sum(map(len, str1.split()))

res6 = 0
for item in str1:
    if item == ' ':
        continue
    res6 += 1

print('The characters frequency avoiding spaces:\n',
      res1, '\n', res2, '\n', res3, '\n', res4, '\n', res5, '\n', res6)

'''
# Python3 code to avoid spaces in characters frequency

str1 = 'geeksforgeeks 33 is best'

# printing original string
# print('The original string is:', str(str3))

str11 = str1.replace(' ','')

res1 = len(str11)

# Python3 code to avoid spaces in characters frequency using isspace() + sum()

# str1 = 'geeksforgeeks 33 is best'

# printing original string
# print('The original string is:', str(str1))

# isspace() checks for space
# sum checks count

res2 = sum(not item.isspace() for item in str1)

# print('The characters frequency avoiding spaces:', res1)

# Using a list comprehension and the join() function

# str5 = 'geeksforgeeks 33 is best'

# printing original string
# print('The original string is:', str(str5))

# using a list comprehension and the join() function

res3 = len(''.join([item for item in str1 if item != ' ']))

str13 = str1.translate({ord(item): None for item in ' '})

res4 = len(str13)

# Version 2: Python3 code to avoid spaces in characters frequency using sum() + len() + map() + split()

# str2 = 'geeksforgeeks 33 is best'

# printing original string
# print('The original string is:', str(str2))

# len() finds individual word frequency
# sum() extracts final frequency

res5 = sum(map(len, str1.split()))

# print('The characters frequency avoiding spaces:', res2)

# print('The characters frequency avoiding spaces:', res3)

# Version 4: Python3 code to avoid spaces in characters frequency

# str4 = 'geeksforgeeks 33 is best'

# printing original string
# print('The original string is:', str4)

res6 = 0
for item in str1:
    if item == ' ':
        continue
    res6 += 1

print('The characters frequency avoiding spaces:\n',
      res1, '\n', res2, '\n', res3, '\n', res4, '\n', res5, '\n', res6)
'''
