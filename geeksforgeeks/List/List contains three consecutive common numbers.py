import itertools

arr1 = [1, 1, 1, 64, 23, 64, 22, 22, 22]

size = len(arr1)

for num in range(size - 2):
	if arr1[num] == arr1[num + 1] and arr1[num + 1] == arr1[num + 2]:
		print(arr1[num])

for num in range(size - 2):
	nums = set([arr1[num], arr1[num + 1], arr1[num + 2]])
	if(len(nums) == 1):
			print(arr1[num])

triples = zip(arr1, arr1[1:], arr1[2:])

print(*[x for x, y, z in itertools.islice(triples, size) if x == y == z])

'''
# Version 1
# creating the array

arr1 = [1, 1, 1, 64, 23, 64, 22, 22, 22]

size = len(arr1) # size of the list

for num in range(size - 2): # looping till length - 2
	if arr1[num] == arr1[num + 1] and arr1[num + 1] == arr1[num + 2]: # checking the conditions
		print(arr1[num]) # printing the element as the conditions are satisfied

# Version 2: using set() function
# creating the array
# arr2 = [1, 1, 1, 64, 23, 64, 22, 22, 22]

# size of the list
# size = len(arr2)

# looping till length - 2

for num in range(size - 2):
	nums = set([arr1[num], arr1[num + 1], arr1[num + 2]])
	if(len(nums) == 1):
			print(arr1[num])

# Version 3: sing itertools library
import itertools
# creating the array
# arr3 = [1, 1, 1, 64, 23, 64, 22, 22, 22]

triples = zip(arr1, arr1[1:], arr1[2:])

print(*[x for x, y, z in itertools.islice(triples, size) if x == y == z])
'''
