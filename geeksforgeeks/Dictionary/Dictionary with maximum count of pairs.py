list1 = [{'gfg': 2, 'best': 4}, {'gfg': 2, 'is': 3, 'best': 4}, {'gfg': 2}]

res1 = max(list1, key=len)

res2 = {}
max_len = 0
for ele in list1:
    if len(ele) > max_len:
        res2 = ele
        max_len = len(ele)

print('Maximum keys dictionary:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Dictionary with maximum keys
# Using max() + key = len

# initializing list

list1 = [{'gfg': 2, 'best': 4}, {'gfg': 2, 'is': 3, 'best': 4}, {'gfg': 2}]

# printing original list
# print("The original list is : " + str(test_list))

# maximum length dict using len param

res1 = max(list1, key=len)

# print('Maximum keys dictionary:', str(res1))

# Python3 code to demonstrate working of
# Dictionary with maximum keys
# Using loop + len()

# initializing list
# test_list = [{"gfg": 2, "best": 4}, {"gfg": 2, "is": 3, "best": 4}, {"gfg": 2}]

# printing original list
# print("The original list is : " + str(test_list))

res2 = {}
max_len = 0
for ele in list1:
    if len(ele) > max_len: # checking for lengths
        res2 = ele
        max_len = len(ele)

print('Maximum keys dictionary:\n', res1, '\n', res2)
'''
