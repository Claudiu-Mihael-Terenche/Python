list1 = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]

list1.sort(key=lambda sub: max(sub), reverse=True)

def get_max(sub): return max(sub)

list2 = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]

list2.sort(key=get_max, reverse=True)

print('Sorted tuples:\n', list1, '\n', list2)

'''
# Python3 code to demonstrate working of
# Sort Tuples by Maximum element
# Using sort() + lambda + reverse

list1 = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]

# printing original list
# print("The original list is : " + str(test_list))

# lambda function getting maximum elements
# reverse for sorting by max - first element's tuples

list1.sort(key=lambda sub: max(sub), reverse=True)

# print('Sorted tuples:', list1)

# Python3 code to demonstrate working of
# Sort Tuples by Maximum element
# Using max() + sort()

# helper function

def get_max(sub): return max(sub)

list2 = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]

# printing original list
# print("The original list is : " + str(test_list))

# sort() is used to get sorted result
# reverse for sorting by max - first element's tuples

list2.sort(key=get_max, reverse=True)

print('Sorted tuples:\n', list1, '\n', list2)
'''
