list1 = [5, 6, [], 3, [], [], 9]

res1 = list(filter(None, list1))

res2 = [num for num in list1 if num != []]

list3 = [5, 6, [], 3, [], [], 9]

while [] in list3:
    list3.remove([])

res4 = [num for i, num in enumerate(list1) if num != []]

print('List after empty list removal:\n', res1, '\n', res2, '\n', list3, '\n', res4)

'''
# Python3 code to remove empty list from list using filter() method

# initializing list by custom values

list1 = [5, 6, [], 3, [], [], 9]

# printing original list
# print("The original list is : " + str(list1))

# removing empty list from list using filter() method

res1 = list(filter(None, list1))

# printing the resultant list
# print('List after empty list removal:', res1)

# Version 2: Python3 code to remove empty list from list using list comprehension

# initializing list
# list2 = [5, 6, [], 3, [], [], 9]

# printing original list
# print('The original list is:', + str(list2))

# remove empty list from list using list comprehension

res2 = [num for num in list1 if num != []]

# printing result
# print('List after empty list removal:', res2)

# Version 3: Python3 code to remove empty list using remove() method

# initializing list

list3 = [5, 6, [], 3, [], [], 9]

# printing original list
# print("The original list is : " + str(list3))

# remove empty list from list using remove()

while [] in list3:
list3.remove([])

# printing result
# print('List after empty list removal:', list3)

# Version 4: using enumerate function

# list4 = [5, 6, [], 3, [], [], 9]

res4 = [num for i, num in enumerate(list1) if num != []]

print('List after empty list removal:\n', res1, '\n', res2, '\n', list3, '\n', res4)
'''
