list1 = [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]

res = dict()
for idx in range(1, max(list1) + 1): res[idx] = sum(key % idx == 0 for key in list1)

print('The constructed dictionary:', res)

'''
# Python3 code to demonstrate working of
# Factors Frequency Dictionary
# Using sum() + loop

# initializing list

list1 = [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]

# printing original list
# print("The original list : " + str(test_list))

res = dict()
for idx in range(1, max(list1) + 1): res[idx] = sum(key % idx == 0 for key in list1)
# using sum() instead of loop for sum computation

print('The constructed dictionary:', res)
'''
