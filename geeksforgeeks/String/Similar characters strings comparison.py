from collections import Counter

str1 = 'e:e:k:s:g'; str2 = 'g:e:e:k:s'

delim = ':'

res1 = sorted(str1.split(':')) == sorted(str2.split(delim))

dict1 = {}; dict2 = {}
dict1 = Counter(str1); dict2 = Counter(str2)

res2 = dict1 == dict2

list1 = str1.split(delim)
list2 = str2.split(delim)

res3 = all(item in list2 for item in list1) and all(item in list1 for item in list2)

print('Are strings similar:\n', res1, '\n', res2, '\n', res3)

'''
# Python3 code to do similar characters strings comparison using split() + sorted()

# initializing strings
str1 = 'e:e:k:s:g'
str2 = 'g:e:e:k:s'

# printing original strings
# print('The original string 1 is:', str(str1))
# print('The original string 2 is:', str(str2))

# initializing delim
delim1 = ':'

# == operator is used for comparison
res1 = sorted(str1.split(':')) == sorted(str2.split(delim1))

# printing result
print('Are strings similar:', str(res1))

# Version 2: using the Counter() function from the collections module
# importing the collections module
from collections import Counter

# initializing strings
str21 = 'e:k:s:g'
str22 = 'g:e:k:s'

# printing original strings
# print('The original string 1 is:', str(str21))
# print('The original string 2 is:', str(str22))

# initializing empty dictionaries
dict1 = {}
dict2 = {}

# counting the frequency of each character in both strings
# and storing the results in the corresponding dictionary
dict1 = Counter(str21)
dict2 = Counter(str22)

# comparing the two dictionaries to check if they have the same keys with the same frequency of values
res2 = dict1 == dict2

# printing result
print('Are strings similar:', str(res2))

# Version 3: using list comprehension and all()
# initializing strings
str31 = 'e:k:s:g'
str32 = 'g:e:k:s'

# initializing delimiter
delim3 = ':'

# convert strings to lists of characters
list1 = str31.split(delim3)
list2 = str32.split(delim3)

# check if both lists have the same characters
res3 = all(item in list2 for item in list1) and all(item in list1 for item in list2)

# printing result
print('Are strings similar:', str(res3))
'''
