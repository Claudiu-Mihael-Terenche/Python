import operator as op
from collections import Counter
from itertools import chain
list1 = ['geeksforgeeks is best for geeks']
item_list = ['e', 'b', 'g']

d1 = dict()
for item in item_list:
    d1[item] = list1[0].count(item)
res1 = d1

d2 = dict()
for item in item_list:
    d2[item] = op.countOf(list1[0], item)
res2 = d2

res3 = {key: val for key, val in dict(Counter(''.join(list1))).items() if key in item_list}

res4 = {key: val for key, val in dict(Counter(chain.from_iterable(list1))).items() if key in item_list}

res5 = {}
for item in ''.join(list1):
    if item in item_list:
        if item in res5:
            res5[item] += 1
        else:
            res5[item] = 1

print('Specific characters frequencies:\n', res1, '\n', res2, '\n', res3, '\n', res4, '\n', res5)

'''
# Python3 code to print specific characters frequency in string list using operator.countOf()
import operator as op

# initializing lists
list4 = ['geeksforgeeks is best for geeks']

# printing original list
# print('The original list:', str(list4))

# char list
item_list4 = ['e', 'b', 'g']

d4 = dict()
for item4 in item_list4:
    d4[item4] = op.countOf(list4[0], item4)
res4 = d4

# printing result
print('Specific characters frequencies:', str(res4))

# Python3 code to demonstrate to print specific characters frequency in string list
# using join() + Counter()
from collections import Counter

# initializing lists
list1 = ['geeksforgeeks is best for geeks']

# printing original list
# print('The original list:', str(list1))

# char list
item_list1 = ['e', 'b', 'g']

# dict comprehension to retrieve on certain frequencies
res1 = {key1: val1 for key1, val1 in dict(Counter(''.join(list1))).items() if key1 in item_list1}

# printing result
print('Specific characters frequencies:', str(res1))

# Python3 code to print specific characters frequency in string list
# using chain.from_iterable() + Counter() + dictionary comprehension
from collections import Counter
from itertools import chain

# initializing lists
list2 = ['geeksforgeeks is best for geeks']

# printing original list
# print('The original list:', str(list2))

# char list
item_list2 = ['e', 'b', 'g']

# dict comprehension to retrieve on certain frequencies from_iterable to flatten / join
res2 = {key2: val2 for key2, val2 in dict(Counter(chain.from_iterable(list2))).items() if key2 in item_list2}

# printing result
print('Specific characters frequencies:', str(res2))

# Python3 code to print specific characters frequency in string list using count()

# initializing lists
list3 = ['geeksforgeeks is best for geeks']

# printing original list
# print('The original list:', str(list3))

# char list
item_list3 = ['e', 'b', 'g']

d3 = dict()
for item3 in item_list3:
    d3[item3] = list3[0].count(item3)
res3 = d3

# printing result
print('Specific characters frequencies:', str(res3))

# Using loop and conditional statement
# initializing lists
list5 = ['geeksforgeeks is best for geeks']

# printing original list
# print('The original list:', str(list5))

# char list
item_list5 = ['e', 'b', 'g']

# initializing dictionary for result
res5 = {}

# loop through each character in the list5 and count their frequency
for item5 in ''.join(list5):
    if item5 in item_list5:
        if item5 in res5:
            res5[item5] += 1
        else:
            res5[item5] = 1

# printing result
print('Specific characters frequencies:', str(res5))
'''
