list1 = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]

K = 1

res1 = [abs(x[K] - y[K]) for x, y in zip(list1, list1[1:])] # zip used to pair each tuple with subsequent tuple

res2 = [abs(list1[i][K] - list1[i + 1][K]) for i in range(len(list1) - K)]

print('Resultant tuple list:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Consecutive Kth column Difference in Tuple List
# Using zip() + list comprehension

list1 = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]

# printing original list
# print("The original list is : " + str(test_list))

K = 1

res1 = [abs(x[K] - y[K]) for x, y in zip(list1, list1[1:])] # zip used to pair each tuple with subsequent tuple

# print('Resultant tuple list:', res1)

# Python3 code to demonstrate working of
# Consecutive Kth column Difference in Tuple List
# Using list slicing

# initializing list
# test_list = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]

# printing original list
# print("The original list is : " + str(test_list))

# initializing K
# K = 1

# using list slicing to get Kth column difference

res2 = [abs(list1[i][K] - list1[i + 1][K]) for i in range(len(list1) - K)]

print('Resultant tuple list:\n', res1, '\n', res2)
'''
