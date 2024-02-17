list1 = [(4, 5, 6, 4, 4), (4, 4, 3), (4, 4, 4), (3, 4, 9)]
K = 4
N = 3

res = [item for item in list1 if item.count(K) == N]

print('Filtered tuples:', res)

'''
# Python3 code to retain records with N occurrences of K using count() + list comprehension

# initializing list

list1 = [(4, 5, 6, 4, 4), (4, 4, 3), (4, 4, 4), (3, 4, 9)]

# printing original list
# print('The original list is:', + str(list1))

# initializing K

K = 4

N = 3

# retain records with N occurrences of K using count() + list comprehension
res = [item for item in list1 if item.count(K) == N]

print('Filtered tuples:', res)
'''
