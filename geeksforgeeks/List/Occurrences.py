list1 = ['a', 'd', 'd', 'c', 'a', 'b', 'b', 'a', 'c', 'd', 'e']
item = 'a'

res = list1.count(item)

print(item, 'occurred', res, 'times')

'''
import operator as op
from collections import Counter

occurrence = {item: list1.count(item) for item in list1}

res1 = occurrence.get(item)

print(item, 'has occurred', res1, 'times')


def countItem(list1, item):
    return list1.count(item)


print('{} has occurred {} times'.format(item, countItem(list1, item)))

items = Counter(list1)

print('{} has occurred {} times'.format(item, items[item]))

print(f'{item} has occurred {op.countOf(list1, item)} times')

# Python code to count the number of occurrences using dictionary comprehension

list1 = ['a', 'd', 'd', 'c', 'a', 'b', 'b', 'a', 'c', 'd', 'e']

item = 'a'

occurrence = {item: list1.count(item) for item in list1}

res1 = occurrence.get(item)

print(item, 'has occurred', res1, 'times')

# Version 2: using count()
def countItem(list1, item):
return list1.count(item)


# driver Code
# list2 = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# num2 = 8

print('{} has occurred {} times'.format(item, countItem(list1, item)))

# Version 3: using counter()
from collections import Counter

# declaring the list
# list3 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

# driver program
# num3 = 3

items = Counter(list1)

print('{} has occurred {} times'.format(item, items[item]))

# Version 4: using countOf()
import operator as op

# declaring the list
# list4 = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]

# driver program
# num4 = 2

print(f'{item} has occurred {op.countOf(list1, item)} times')
'''
