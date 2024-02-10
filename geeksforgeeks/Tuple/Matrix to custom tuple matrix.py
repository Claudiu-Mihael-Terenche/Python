list1 = [[4, 5, 6], [6, 7, 3], [1, 3, 4]]

add_list = ['Gfg', 'is', 'best']

res = [(ele1, ele2) for ele1, sub in zip(add_list, list1) for ele2 in sub]

print('Matrix after conversion:', res)

'''
# Python3 code to demonstrate working of
# Convert Matrix to Custom Tuple Matrix
# Using list comprehension + zip()

list1 = [[4, 5, 6], [6, 7, 3], [1, 3, 4]]

# printing original list
# print("The original list is : " + str(test_list))

add_list = ['Gfg', 'is', 'best']

# Convert matrix to custom tuple matrix using list comprehension + zip()
res = [(ele1, ele2) for ele1, sub in zip(add_list, list1) for ele2 in sub]

print('Matrix after conversion:', res)
'''
