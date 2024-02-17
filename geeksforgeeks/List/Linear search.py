list1 = [10, 20, 80, 30, 60, 50, 110, 100, 130, 110, 170]
x = 110

res = []
for i in range(len(list1)):
    if list1[i] == x:
        res.append(i)

print(*res)

'''
# Searching an element in a list/array in python
# can be simply done using \'in\' operator
# Example:
# if x in arr:
# print arr.index(x)

# If you want to implement Linear Search in python

# Linearly search x in arr[]
# If x is present then return its location
# else return -1

def search(arr, x):

	for i in range(len(arr)):

		if arr[i] == x:
			return i

	return -1
'''
