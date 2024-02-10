from collections import Counter

list1 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

res1 = list(set([num for num in list1 if list1.count(num) > 1]))

items = Counter(list1)

print(items)

res2 = list([num for num in items if items[num] > 1])

print('', res1, '\n', res2)

'''
# Using list comprehension method

list1 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

res1 = list(set([num for num in list1 if list1.count(num) > 1]))

# print(res1)

# Version 2: using counter function from collection module

from collections import Counter

# list2 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]

items = Counter(list1)

print(items)

res2 = list([num for num in items if items[num] > 1])

print('', res1, '\n', res2)
'''
