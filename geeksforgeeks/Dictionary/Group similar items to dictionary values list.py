from collections import defaultdict
list1 = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]

res = defaultdict(list)
for ele in list1:
    res[ele].append(ele)

print('Similar grouped dictionary:', dict(res))

'''
# Python3 code to demonstrate working of
# Group Similar items to Dictionary Values List
# Using defaultdict + loop
from collections import defaultdict

list1 = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]

# printing original list
# print("The original list : " + str(test_list))

# using defaultdict for default list

res = defaultdict(list)
for ele in list1: res[ele].append(ele) # appending similar values

print('Similar grouped dictionary:', dict(res))
'''
