list1 = [4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]; list2 = [9, 9, 74, 21, 45, 11, 63]

res1 = list(set(list1).intersection(list2))

print(res1)

res2 = list(set(list1) & set(list2))

print(res2)

res3 = [value for value in list1 if value in list2]

print(res3)

'''
# Python program to illustrate the intersection of two lists using set() and intersection()
#def Intersection(lst1, lst2):
    # return set(lst1).intersection(lst2)

list1 = [4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
list2 = [9, 9, 74, 21, 45, 11, 63]

res1 = list(set(list1).intersection(list2))

print(res1)

# print(Intersection(lst1, lst2))

# Python program to illustrate the intersection
# of two lists using set() method
# def intersection(lst1, lst2):
	# return list(set(lst1) & set(lst2))

# Driver Code
# lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
# lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
# print(intersection(lst1, lst2))

res2 = list(set(list1) & set(list2))

print(res2)

# Python program to illustrate the intersection
# of two lists in most simple way
# def intersection(lst1, lst2):
	# lst3 = [value for value in lst1 if value in lst2]
	# return lst3

# Driver Code
# lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
# lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
# print(intersection(lst1, lst2))

res3 = [value for value in list1 if value in list2]

print(res3)
'''
