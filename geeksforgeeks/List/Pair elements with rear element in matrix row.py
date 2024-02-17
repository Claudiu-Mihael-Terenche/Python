list1 = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]

res1 = []
for sub in list1:
    res1.append([[num, sub[-1]] for num in sub[:-1]])

res2 = [[(num, sub[-1]) for num in sub[:-1]] for sub in list1]

print('The list after pairing is:\n', res1, '\n', res2)

'''
# Python3 code to pair elements with rear element in matrix row using list comprehension

# initializing list

list1 = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]

# printing original list
# print("The original list is : " + str(list1))

# pair elements with rear element in matrix row using list comprehension

res1 = []
for sub in list1: res1.append([[num, sub[-1]] for num in sub[:-1]])

# printing result
# print('The list after pairing is:', str(res1))

# Version 2: Python3 code to pair elements with rear element in matrix row using list comprehension with 
# tuple packing and unpacking

# initializing list
# list2 = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]

# printing original list
# print("The original list is : " + str(list2))

# pair elements with rear element in matrix row using list comprehension with tuple packing and unpacking

res2 = [[(num, sub[-1]) for num in sub[:-1]] for sub in list1]

print('The list after pairing is:\n', res1, '\n', res2)
'''
