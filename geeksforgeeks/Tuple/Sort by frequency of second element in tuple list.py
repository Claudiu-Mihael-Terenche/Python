from collections import Counter

list1 = [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]

freq_map = Counter(val for key, val in list1)

res = sorted(list1, key=lambda ele: freq_map[ele[1]], reverse=True)

print('Sorted list of tuples:', res)

'''
# Python3 code to demonstrate working of
# Sort by Frequency of second element in Tuple List
# Using Counter() + lambda + sorted()
from collections import Counter

list1 = [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]

# printing original list
# print("The original list is : " + str(test_list))

# constructing mapping using Counter

freq_map = Counter(val for key, val in list1)

res = sorted(list1, key=lambda ele: freq_map[ele[1]], reverse=True) # performing sort of result

print('Sorted list of tuples:', res)
'''
