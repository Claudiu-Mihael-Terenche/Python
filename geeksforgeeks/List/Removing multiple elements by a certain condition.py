list1 = [11, 5, 17, 18, 23, 50]

res1 = [num for num in list1 if num % 2 != 0]

print(*res1)

unwanted_nums = {11, 5}

res2 = [num for num in list1 if num not in unwanted_nums]

print('New list after removing unwanted numbers:', *res2)

list3 = [11, 5, 17, 18, 23, 50]

del list3[1:5]

print(*list3)

list4 = [11, 5, 17, 18, 23, 50]

unwanted = [0, 3, 4]

for num in sorted(unwanted, reverse=True): del list4[num]

print (*list4)

'''
# Python program to remove multiple elements from a list using list comprehension

# creating a list

list1 = [11, 5, 17, 18, 23, 50]

res1 = [num for num in list1 if num % 2 != 0] # will create a new list, excluding all even numbers

print(*res1)

# Version 2: Python program to remove multiple elements from a list using list comprehension

# creating a list
# list1_2 = [11, 5, 17, 18, 23, 50]

# items to be removed

unwanted_nums = {11, 5}

res2 = [num for num in list1 if num not in unwanted_nums]

print('New list after removing unwanted numbers:', *res2) # printing modified list

# Version 3: Python program to remove multiple elements from a list using list slicing

# creating a list

list3 = [11, 5, 17, 18, 23, 50]

# removes elements from index 1 to 4
# i.e. 5, 17, 18, 23 will be deleted

del list3[1:5]

print(*list3)

# Version 4: Python program to remove multiple elements from a list when the index is known

# creating a list

list4 = [11, 5, 17, 18, 23, 50]

unwanted = [0, 3, 4] # given index of elements, removes 11, 18, 23

for num in sorted(unwanted, reverse = True):
	del list4[num]

print (*list4) # printing modified list
'''
