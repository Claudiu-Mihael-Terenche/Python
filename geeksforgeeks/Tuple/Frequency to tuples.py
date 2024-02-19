from collections import Counter
list1 = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]

res = [(*key, val) for key, val in Counter(list1).items()]

print('Frequency tuple list:', res)

'''
# Python3 code to demonstrate working of assign frequency to tuples using Counter() + items() + * operator 
+ list comprehension
from collections import Counter

list1 = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]

# printing original list
# print("The original list is : " + str(list1))

# one-liner to solve problem
# assign frequency as last element of tuple

res = [(*key, val) for key, val in Counter(list1).items()]

print('Frequency tuple list:', res)
'''
