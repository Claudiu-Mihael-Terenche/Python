from itertools import chain

list1 = [[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]

res1 = list(zip(*chain.from_iterable(list1)))

res2 = list(zip(*[ele for sub in list1 for ele in sub]))

matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

res3 = list(tuple(map(lambda x: tuple(list(x)), matrix)))

print('\n', res1, '\n', res2, '\n', res3) # Output: ([1, 2, 3], [4, 5, 6], [7, 8, 9])

'''
# Python3 code to demonstrate working of
# Convert Tuple Matrix to Tuple List
# Using chain.from_iterable() + zip()
from itertools import chain

list1 = [[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]

# printing original list
# print("The original list is : " + str(test_list))

# flattening using from_iterable

res1 = list(zip(*chain.from_iterable(list1)))

# print('The converted tuple list:', res1)

# Python3 code to demonstrate working of
# Convert Tuple Matrix to Tuple List
# Using list comprehension + zip()

# initializing list
# test_list = [[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]

# printing original list
# print("The original list is : " + str(test_list))

# flattening
# temp = [ele for sub in list1 for ele in sub]
# res3 = list(zip(*temp))

# joining to form column pairs

res2 = list(zip(*[ele for sub in list1 for ele in sub]))

# print('The converted tuple list:', res2)

# Using lambda function

matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

res3 = list(tuple(map(lambda x: tuple(list(x)), matrix)))

print('\n', res1, '\n', res2, '\n', res3) # Output: ([1, 2, 3], [4, 5, 6], [7, 8, 9])
'''
