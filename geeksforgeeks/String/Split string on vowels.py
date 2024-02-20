import re
# Python3 code to split string on vowels using split() + regex
str1 = 'GFGABste4oCS'

res1 = re.split('[aeiou]', str1.lower())

print('The split string:', str(res1))
