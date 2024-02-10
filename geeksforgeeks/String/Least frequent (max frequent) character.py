from collections import Counter

# Python 3 code to print the least frequent character in string using collections.Counter() + min()/max()

str1 = 'GeeksforGeeks'

# using collections.Counter() + min() to get least frequent character in string
min1 = min(Counter(str1), key=Counter(str1).get)
max1 = max(Counter(str1), key=Counter(str1).get)

min2 = min(str1, key=lambda item: str1.count(item))
max2 = max(str1, key=lambda item: str1.count(item))

print('Max freq of a char:\n', max1, '\n', max2, '\nMin freq of a char:\n', min1, '\n', min2)
