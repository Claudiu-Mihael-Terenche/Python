from collections import Counter
import re

# Using Counter() + list comprehension + re.findall()

str1 = 'Geeksforgeeks is best for geeks. A geek should take interest.'

word = 'geek'

res = dict(Counter(re.findall(f'{word}(.)', str1, flags=re.IGNORECASE)))

print('The characters frequency is:', res)
