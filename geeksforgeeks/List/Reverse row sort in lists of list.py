list1 = [[4, 1, 6], [7, 8], [4, 10, 8]]

res1 = [sorted(sub, reverse=True) for sub in list1]

for num in list1:
    num.sort(reverse=True)

print('The reverse sorted matrix is:\n', res1, '\n', list1)

'''
# Python3 code to reverse row sort in lists of list using list comprehension + sorted()

list1 = [[4, 1, 6], [7, 8], [4, 10, 8]]

# printing original list
# print('The original list is:', str(list1))

# reverse row sort in lists of list using list comprehension + sorted()

res1 = [sorted(sub, reverse=True) for sub in list1]

# printing result
# print('The reverse sorted matrix is:', res1)

# Version 2: Python3 code to reverse row sort in lists of list using loop + sort() + reverse

# initializing list
# list2 = [[4, 1, 6], [7, 8], [4, 10, 8]]

# printing original list
# print("The original list is : " + str(list2))

# reverse row sort in lists of list using loop

for num in list1: num.sort(reverse=True)

print('The reverse sorted matrix is:\n', res1, '\n', list1)
'''
