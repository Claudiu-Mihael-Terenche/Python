list1 = [(15, 3), (3, 9), (1, 10), (99, 2)]

temp = ''.join([str(ele) for sublist in list1 for ele in sublist])

res1 = sorted(set(temp))

res1 = [int(ele) for ele in res1]

res1 = list(res1)

item = ''
for sub in list1:
	for ele in sub:
		item += str(ele)
res2 = sorted(list(map(int, set(item))))

print('The extracted digits:\n', res1, '\n', res2)

'''
# Using list Comprehension

list1 = [(15, 3), (3, 9), (1, 10), (99, 2)]

# Printing original list
# print("The original list is : " + str(test_list))

# Extracting digits from Tuple list using list comprehensions

temp = ''.join([str(ele) for sublist in list1 for ele in sublist])
res1 = sorted(set(temp))
res1 = [int(ele) for ele in res1]
res1 = list(res1)

# print('The extracted digits:', res1)

# Python3 code to demonstrate working of
# Extract digits from Tuple list

# test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]

# printing original list
# print("The original list is : " + str(test_list))

item = ''
for sub in list1: # extract digits from tuple list
	for ele in sub:
		item += str(ele)
res2 = sorted(list(map(int, set(item))))

print('The extracted digits:\n', res1, '\n', res2)
'''
