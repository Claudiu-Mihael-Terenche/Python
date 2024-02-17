list1 = [(4, 5, 6, 3), (5, 6, 6, 9), (1, 3, 5, 6), (6, 6, 7, 8)]
K = 6

res = [idx for idx in list1 if (K, K) not in zip(idx, idx[1:])]

print('The records after removal:', res)

'''
# Python3 code to remove consecutive K element records sing zip() + list comprehension

# initializing list

list1 = [(4, 5, 6, 3), (5, 6, 6, 9), (1, 3, 5, 6), (6, 6, 7, 8)]

# printing original list
# print("The original list is : " + str(list1))

# initializing K

K = 6

# remove consecutive K element records using zip() + list comprehension
res = [idx for idx in list1 if (K, K) not in zip(idx, idx[1:])]

print('The records after removal:', res)
'''
