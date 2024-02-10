list1 = [(3, 4), (1, 2), (4, 3), (5, 6)]

res = len(list(set(tuple(sorted(sub)) for sub in list1)))

print('Unique tuples frequency:', res)

'''
# Python3 code to demonstrate working of
# Unique Tuple Frequency [ Order Irrespective ]
# Using tuple() + list comprehension + sorted() + len()

list1 = [(3, 4), (1, 2), (4, 3), (5, 6)]

# printing original list
# print("The original list is : " + str(test_list))

# Using tuple() + list comprehension + sorted() + len()
# Size computed after conversion to set

res = len(list(set(tuple(sorted(sub)) for sub in list1)))

print('Unique tuples frequency:', res)
'''
