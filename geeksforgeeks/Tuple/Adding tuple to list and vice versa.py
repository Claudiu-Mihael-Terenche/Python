list1 = [5, 6, 7]
list2 = [5, 6, 7]
list3 = [5, 6, 7]

tup = (9, 10)

list2 += tup

list3.extend(list(tup))

res = tuple(list(tup) + list1)

tup1 = list(tup)
tup1.extend(list1)
tup1 = tuple(tup1)

print('The container after addition:\n', list2, '\n', list3, '\n', res, '\n', tup1)

'''
# Method 1 : Using += operator [list + tuple]

# initializing list

list0 = [5, 6, 7]; list1 = [5, 6, 7]; list3 = [5, 6, 7]

# printing original list
# print("The original list is : " + str(list1))

# initializing tuple

tup0 = (9, 10)

# adding tuple to list and vice - versa using += operator (list + tuple)
list1 += tup0

# print('The container after addition:', list1)

# Method #2 : Using tuple(), data type conversion [tuple + list]

#list2 = [5, 6, 7]

# printing original list
# print("The original list is : " + str(list2))

# tup2 = (9, 10)

# adding tuple to list and vice - versa using tuple(), data type conversion [tuple + list]

res2 = tuple(list(tup0) + list0)

# print('The container after addition:', res2)

# Method #3: Using tuple(),list() and extend() methods

# list3 = [5, 6, 7]

# tup3 = (9,10)

# printing original list
# print("The original list is : " + str(list3))

# adding tuple to list

list3.extend(list(tup0))

# print('The container after addition:', list3)

# list32 = [1,2,3,4]

# tup32 = (5,6)

# printing original tuple
# print("The original tuple is : " + str(tup32))

# adding list to tuple

tup4 = list(tup0)
tup4.extend(list0)
tup4 = tuple(tup4)

print('The container after addition:\n', list1, '\n', res2, '\n', list3, '\n', tup4)

# METHOD 4:Using the insert() method

list4 = [5, 6, 7]
tup4 = (9, 10)

index = 3
list4.insert(index, tup4)

print('List after addition:', list4)
'''
