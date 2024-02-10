list1 = [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]

ele = 3

K = 1

res = list(filter(lambda tup: tup[K] == ele, list1))

print('The tuples of element at Kth position:', res)

'''
# Python3 code to do records with value at K index using map() and lambda function

list1 = [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]

# printing original list
# print("The original list is : " + str(list1))

ele = 3

K = 1

# records with value at K index using map() and lambda function
res = list(filter(lambda tup: tup[K] == ele, list1))

print('The tuples of element at Kth position:', res)
'''
