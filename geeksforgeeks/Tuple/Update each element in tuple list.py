list1 = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]

add_ele = 4

res1 = [tuple(j + add_ele for j in sub ) for sub in list1]

res2 = [tuple(map(lambda ele: ele + add_ele, sub)) for sub in list1]

print('List after bulk update:\n', res1, '\n', res2, '\n')

updated_list1 = [(a + 1, b + 1, c + 1) for idx, (a, b, c) in enumerate(list1)]

print('The updated list using enumerate() and tuple unpacking:', updated_list1, '\n')

updated_list2 = [tuple(x + 1 for x in t) for t in zip(*list1)]

print('The updated list using zip() function:', updated_list2, '\n')

list2 = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]

new_elements1 = [(5, 7, 2), (6, 9, 3)]

list2.extend(new_elements1)

print('List after using extend() method:', list2, '\n')

list3 = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]

new_elements2 = (5, 7, 2)

index_to_update = 1

list3 = list3[:index_to_update] + [new_elements2] + list3[index_to_update + 1:]

print('List after using slicing and concatenation:', list3, '\n')

def update_tuples(tuples, new_val):
	for i in range(len(tuples)):
		x, y, z = tuples[i]
		tuples[i] = (new_val, y, z)
	return tuples

tuples = [(1, 56, 'M'), (1, 14, 'F'), (2, 43, 'F'), (2, 10, 'M')]

new_val = 5

updated_tuples = update_tuples(tuples, new_val)

print(updated_tuples)

'''
list1 = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]

add_ele = 4

# Update each element in tuple list using list comprehension
res1 = [tuple(j + add_ele for j in sub ) for sub in list1]

# print('List after bulk update:', res1, '\n')

# add_ele = 4

# Update each element in tuple list sing list comprehension + map() + lambda

res2 = [tuple(map(lambda ele: ele + add_ele, sub)) for sub in list1]

print('List after bulk update:\n', res1, '\n', res2, '\n')

# Using enumerate() method update each element by adding 1 to each value
updated_list1 = [(a + 1, b + 1, c + 1) for idx, (a, b, c) in enumerate(list1)]

print('The updated list using enumerate() and tuple unpacking:', updated_list1, '\n')

# Using Zip() + List Comprehension update each element by adding 1 to each value
updated_list2 = [tuple(x + 1 for x in t) for t in zip(*list1)]

print('The updated list using zip() function:', updated_list2, '\n')

list2 = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]

new_elements1 = [(5, 7, 2), (6, 9, 3)] # new elements to extend the list

list2.extend(new_elements1) # using extend() to update the list

print('List after using extend() method:', list2, '\n')

list3 = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]

new_elements2 = (5, 7, 2) # new elements to replace at a specific index

index_to_update = 1 # index to update

# using slicing and concatenation to update the list
list3 = list3[:index_to_update] + [new_elements2] + list3[index_to_update + 1:]

print('List after using slicing and concatenation:', list3, '\n')

def update_tuples(tuples, new_val):
	for i in range(len(tuples)):
		x, y, z = tuples[i]
		tuples[i] = (new_val, y, z)
	return tuples

tuples = [(1, 56, 'M'), (1, 14, 'F'), (2, 43, 'F'), (2, 10, 'M')]

new_val = 5

updated_tuples = update_tuples(tuples, new_val)

print(updated_tuples)
'''
