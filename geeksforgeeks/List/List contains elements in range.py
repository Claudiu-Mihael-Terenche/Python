list1 = [4, 5, 6, 7, 3, 9]

start, end = 7, 10

res1 = any(start <= num < end for num in list1)

res2 = all(start <= num < end for num in list1)

print('Does list contain: \nany element in range:\n', res1, '\nall elements in range:\n', res2)

res3 = len([num for num in list1 if start > num >= end]) == 0

res4 = res3 == len(list1)

print ('Does list contain: \nall elements in range:\n', res3, '\nall elements in range:\n', res4)

def in_range(num): return start <= num < end

filtered_list = list(filter(in_range, list1))

res5 = bool(filtered_list)

print('Does list contain any element in range:', res5)

'''
# Python3 code to test if list contains elements in range using any()

# initializing list and range boundaries

list1 = [4, 5, 6, 7, 3, 9]
start, end = 7, 10

# checking if any element in the list is within the range / test if list contains elements in range using all()
res1 = any(start <= num < end for num in list1)
res2 = all(start <= num < end for num in list1)

print('Does list contain: \nany element in range:\n', res1, '\nall elements in range:\n', res2)

# Version 2: Python3 code to test if list contains elements in range using all()

# initializing loop
# list2 = [4, 5, 6, 7, 3, 9]

# printing original list
# print("The original list is : " + str(list2))

# initialization of range
# a2, b2 = 7, 10

# test if list contains elements in range using all()
# res2 = all(a <= num < b for num in list1)

# printing result
# print ('Does list contain all elements in range:', str(res))

#Version 3: Python3 code to test if list contains elements in range using list comprehension and len()
#initializing list
# list3 = [4, 5, 6, 7, 3, 9]

#printing original list
# print("The original list is : " + str(list3))

#initialization of range
# a3, b3 = 7, 10

#test if list contains elements in range using list comprehension and len()

res3 = len([num for num in list1 if start > num >= end]) == 0
res4 = res3 == len(list1)

print ('Does list contain: \nall elements in range:\n', res3, '\nall elements in range:\n', res4)

# Version 4: Python3 code to test if list contains elements in range using filter()

# initializing list and range boundaries
# list4 = [4, 5, 6, 7, 3, 9]
# a4, b4 = 7, 10

# function to check if x lies within the given range

def in_range(num): return start <= num < end

filtered_list = list(filter(in_range, list1)) # filtering out the elements that lie within the range

res5 = bool(filtered_list)  # checking if the filtered list is not empty

print('Does list contain any element in range:', res5)
'''
