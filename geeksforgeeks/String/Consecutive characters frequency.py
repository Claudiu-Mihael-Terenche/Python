from itertools import groupby

str1 = 'geekksforgggeeks'

res1 = [len(list(j)) for _, j in groupby(str1)]

import itertools

res2 = [len(list(group)) for key, group in itertools.groupby(str1)]

print('The consecutive characters frequency:\n', res1, '\n', res2)

'''
# Using list comprehension + groupby()
from itertools import groupby

str1 = 'geekksforgggeeks'

# printing original string
# print('The original string is:', str1)

# Consecutive characters frequency

res1 = [len(list(j)) for _, j in groupby(str1)]

# print('The consecutive characters frequency:', res1)

# Version 2
import itertools

# str2 = 'geekksforgggeeks'

# printing original string
# print('The original string is:', str2)

# consecutive characters frequency Using itertools.groupby()

res2 = [len(list(group)) for key, group in itertools.groupby(str1)]

print('The consecutive characters frequency:\n', res1, '\n', res2)
'''
