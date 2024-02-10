# Python program to find the missing and additional elements

list1 = [1, 2, 3, 4, 5, 6]; list2 = [4, 5, 6, 7, 8]

print('list1 - list2 =', *(set(list1).difference(list2)))
print('list2 - list1 =', *(set(list2).difference(list1)))
