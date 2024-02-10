list1 = ['Gfg', 'is', 'Best']

subs_dict = {'Gfg': [5, 6, 7], 'is': [7, 4, 2]}

K = 2

res = [ele if ele not in subs_dict else subs_dict[ele][K] for ele in list1]

print('The list after substitution:', res)

'''
# Python3 code to demonstrate working of
# Replace String by Kth Dictionary value
# Using list comprehension

list1 = ['Gfg', 'is', 'Best']

# printing original list
# print("The original list : " + str(test_list))

subs_dict = {'Gfg': [5, 6, 7], 'is': [7, 4, 2]}

K = 2

# using list comprehension to solve problem using one liner
res = [ele if ele not in subs_dict else subs_dict[ele][K] for ele in list1]

print('The list after substitution:', res)
'''
