import re

# Python3 code to find the longest substring of K using regular expression and max()

str1 = 'abcaaaacbbaa'

K = 'a'

matches = re.findall(K + '+', str1) # find all occurrences of the character

res = len(max(matches, key=len)) # find the length of the longest substring

print('The longest substring length:', res)
