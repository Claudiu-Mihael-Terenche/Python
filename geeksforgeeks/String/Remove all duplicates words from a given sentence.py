from collections import Counter
# Using Counter()
str1 = 'Python is great but Java is not good'

res1 = ' '.join(Counter(str1.split()))

# Using dict

res2 = ' '.join(dict.fromkeys(str1.split()))

print('\n', res1, '\n', res2)

'''
# Using set()

str1 = 'Python is great and Java is also great'

res3 = ' '.join(set(str1.split()))

print(res3)
'''
