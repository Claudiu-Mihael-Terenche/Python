list1 = [('gfg', 1), ('is', 2), ('best', 3)]
list2 = [('i', 3), ('love', 4), ('gfg', 1)]

set1 = set(list1)
set2 = set(list2)

intersection = set1.intersection(set2)

res1 = list(intersection)

res2 = list(filter(lambda item: item in list2, list1))

res3 = [ele1 for ele1 in list1 for ele2 in list2 if ele1 == ele2]

print('The Intersection of data records is:\n', res1, '\n', res2, '\n', res3)

'''
# Python3 code to demonstrate working of
# Intersection in Tuple Records Data
# Using set.intersection()

list1 = [('gfg', 1), ('is', 2), ('best', 3)]
list2 = [('i', 3), ('love', 4), ('gfg', 1)]

# printing original lists
# print("The original list 1 is : " + str(test_list1))
# print("The original list 2 is : " + str(test_list2))

# Intersection in Tuple Records Data
# set.intersection()

set1 = set(list1)
set2 = set(list2)

intersection = set1.intersection(set2)

res1 = list(intersection)

# print('The Intersection of data records is:', res1)

# Using List Comprehension and filter() function:
# test_list1 = [('gfg', 1), ('is', 2), ('best', 3)]
# test_list2 = [('i', 3), ('love', 4), ('gfg', 1)]
# printing original lists
# print("The original list 1 is : " + str(test_list1))
# print("The original list 2 is : " + str(test_list2))

res2 = list(filter(lambda item: item in list2, list1))

# print('The Intersection of data records is:', res2)

# Python3 code to demonstrate working of
# Intersection in Tuple Records Data
# Using list comprehension

# Initializing lists
# test_list1 = [('gfg', 1), ('is', 2), ('best', 3)]
# test_list2 = [('i', 3), ('love', 4), ('gfg', 1)]

# printing original lists
# print("The original list 1 is : " + str(test_list1))
# print("The original list 2 is : " + str(test_list2))

# Intersection in Tuple Records Data
# Using list comprehension

res3 = [ele1 for ele1 in list1 for ele2 in list2 if ele1 == ele2]

print('The Intersection of data records is:\n', res1, '\n', res2, '\n', res3)
'''
