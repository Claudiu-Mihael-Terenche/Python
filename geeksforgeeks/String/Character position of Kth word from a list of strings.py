# Python3 code to find word index for K position in strings list using enumerate() + list comprehension

list1 = ['geekforgeeks', 'is', 'best', 'for', 'geeks']

K = 20

res1 = [item[0] for sub in enumerate(list1) for item in enumerate(sub[1])]

res1 = res1[K]

print('Index of character at Kth position word:', res1)
