import re

# Python3 code to split string on vowels using split() + regex

str1 = 'GFGABste4oCS'

res1 = re.split('a|e|i|o|u', str1.lower())

print('The splitted string:', str(res1))
