import re

# Python3 code for exceptional split in string using regex()

str1 = 'gfg, is, (best, for), geeks'

res1 = re.split(r', ', str1)

print('The string after exceptional split:', res1)
