from itertools import combinations

list1 = [(2, 4), (6, 7), (5, 1), (6, 10)]

res = [(a1 + a2, b1 + b2) for (a1, b1), (a2, b2) in combinations(list1, 2)]

print('The summation combinations are:', res)

'''
# Python3 code to do summation combination in tuple lists using list comprehension + combinations
from itertools import combinations

list1 = [(2, 4), (6, 7), (5, 1), (6, 10)]

# printing original list
# print("The original list : " + str(test_list))

# Summation combination in tuple lists
# Using list comprehension + combinations

res = [(a1 + a2, b1 + b2) for (a1, b1), (a2, b2) in combinations(list1, 2)]

print('The summation combinations are:', res)
'''
