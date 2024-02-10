import copy

list1 = [1, 2, [3,5], 4]

res1 = copy.copy(list1) # using copy for shallow copy

res2 = copy.deepcopy(list1) # using deepcopy

print('', res1, '\n', res2)

'''
# Python code to clone or copy a list using the method of shallow copy

# importing copy module
import copy

list1 = [1, 2, [3,5], 4]

res1 = copy.copy(list1) # using copy for shallow copy
res2 = copy.deepcopy(list1) # using deepcopy

print('', res1, '\n', res2)

# Version 2: using the method of deep copy
# importing copy module
# import copy

# initializing list
# list2 = [1, 2, [3,5], 4]

# using deepcopy for deepcopy
# listCopied2 = copy.deepcopy(list2)
# print(listCopied2)
'''
