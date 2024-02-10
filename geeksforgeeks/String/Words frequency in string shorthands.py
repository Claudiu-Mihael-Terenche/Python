from collections import Counter

str1 = 'Gfg is best. Geeks are good and Geeks like Gfg'

res1 = Counter(str1.split())

print('The words frequency:', str(dict(res1)))

str2 = 'Gfg is best. Geeks are good and Geeks like Gfg'

str22 = str2.split()

freq = {word: str22.count(word) for word in set(str22)}

print('The words frequency:', str(freq))

str3 = 'Gfg is best. Geeks are good and Geeks like Gfg'

res3 = {key: str3.count(key) for key in str3.split()}

print('The words frequency:', res3)

'''
# Using counter() + split()

from collections import Counter

# initializing string
str1 = 'Gfg is best. Geeks are good and Geeks like Gfg'

# printing original string
# print('The original string is:', str(str1))

# words frequency in string shorthands using counter() + split()
res1 = Counter(str1.split())

# printing result
print('The words frequency:', str(dict(res1)))


# Version 2: Using set() and list comprehension
# initializing string
str2 = 'Gfg is best. Geeks are good and Geeks like Gfg'

# printing original string
# print('The original string is:', str(str1))

# Split the string into a list of words
str22 = str2.split()

# using set() and list comprehension to count the frequency of each word
freq = {word: str22.count(word) for word in set(str22)}

# printing result
print('The words frequency:', str(freq))

# Version 3: Using dictionary comprehension + count() + split()

# initializing string
str3 = 'Gfg is best. Geeks are good and Geeks like Gfg'

# printing original string
# print('The original string is:', str(str2))

# words frequency in string shorthands using dictionary comprehension + count() + split()
res3 = {key: str3.count(key) for key in str3.split()}

# printing result
print('The words frequency:', str(res3))
'''
