# Using sort() + count() + lambda

list1 = ['geekforgeeks', 'is', 'best', 'for', 'geeks']

K = 'e'

list1.sort(key=lambda ele: -ele.count(K))

print('Sorted string:', list1)
