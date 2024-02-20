from collections import Counter
# Python3 code to print odd (even) frequency characters using list comprehension + Counter()
str1 = 'geekforgeeks is best for geeks'

res1 = [item for item, count in Counter(str1).items() if count % 2 == 0]
res2 = [item for item, count in Counter(str1).items() if count % 2 != 0]

print('The even frequency characters are:\n', *res1, '\nThe odd frequency characters are:\n', *res2)
