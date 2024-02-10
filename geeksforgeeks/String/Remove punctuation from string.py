import string

str1 = 'Gfg, is best: for ! Geeks ;'

str1 = str1.translate({ord(item): None for item in string.punctuation})

str2 = 'Gfg, is best: for ! Geeks ;'

for punctuation in string.punctuation: str2 = str2.replace(punctuation, '')

str3 = 'Gfg, is best: for ! Geeks ;'

punc = ',:!;'

for item in str3:
	if item in punc:
		str3 = str3.replace(item, '')

str4 = 'Gfg, is best : for ! Geeks ;'

res4 = ' '
for item in str4:
    if item not in punc:
        res4 += item

print('The string after punctuation filter:\n', str1, '\n', str2, '\n', str3, '\n', res4)

'''
import string

str1 = 'Gfg, is best: for ! Geeks ;'

str1 = str1.translate({ord(item): None for item in string.punctuation})
# str1 = str1.translate(str.maketrans('', '', string.punctuation))
# str1 = str1.translate({ord(item): None for item in ',:!;'})
print(str1)

# Version 2: using replace() method
import string

# initializing string
str2 = 'Gfg, is best : for ! Geeks ;'

# printing original string
# print('The original string is:', str2)

# removing punctuations using replace() method
for punctuation in string.punctuation: str2 = str2.replace(punctuation, '')

# printing result
print('The string after punctuation filter:', str2)

# Version 3
# initializing string
str3 = 'Gfg, is best : for ! Geeks ;'

# printing original string
# print('The original string is:', str3)

# initializing punctuations string
punc3 = ',:!;'

# removing punctuations in string using loop + punctuation string
for item3 in str3:
	if item3 in punc3:
		str3 = str3.replace(item3, '')

# printing result
print('The string after punctuation filter:', str3)

# Version 4
# initializing string
str4 = 'Gfg, is best : for ! Geeks ;'

# printing original string
# print('The original string is:', str4)

# initializing punctuations string
punc4 = ',:!;'
res4 = ' '

for item4 in str4:
    if item4 not in punc4:
        res4 += item4

# printing result
print('The string after punctuation filter:', res4)
'''
