list1 = [1, 5, 10, 20, 40, 80, 100]
list2 = [6, 7, 20, 80, 100]
list3 = [3, 4, 15, 20, 30, 70, 80, 120]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

set1 = set1.intersection(set2)
set1 = set1.intersection(set3)

print(list(set1))

res2 = [elem for elem in set1 if elem in set2 and elem in set3]

print(res2)

res3 = list(filter(lambda x: x in list2 and x in list3, list1))

print(res3)

res4 = []
for i in list1:
        if i in list2 and i in list3:
            res4.append(i)

print(list(set(res4)))

res5 = set()
for elem in list1:
    if elem in list2 and elem in list3:
        res5.add(elem)

print(list(res5))

'''
# Python3 program to find common elements 
# in three lists using sets

def IntersecOfSets(arr1, arr2, arr3):
    # Converting the arrays into sets
    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)

    # Calculates intersection of 
    # sets on s1 and s2
    set1 = s1.intersection(s2)  # [80, 20, 100]

    # Calculates intersection of sets
    # on set1 and s3
    result_set = set1.intersection(s3)

    # Converts resulting set to list
    final_list = list(result_set)
    print(final_list)


# Driver Code
if __name__ == '__main__':
    # Elements in Array1
    arr1 = [1, 5, 10, 20, 40, 80, 100]

    # Elements in Array2
    arr2 = [6, 7, 20, 80, 100]

    # Elements in Array3
    arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

    # Calling Function
    IntersecOfSets(arr1, arr2, arr3)
    
def find_common(list1, list2, list3):
	# Convert lists to sets
	set1 = set(list1)
	set2 = set(list2)
	set3 = set(list3)
	
	# Use list comprehension to find common elements
	# in all three sets and return as a list
	return [elem for elem in set1 if elem in set2 and elem in set3]

list1 = [1, 5, 10, 20, 40, 80]
list2 = [6, 7, 20, 80, 100]
list3 = [3, 4, 15, 20, 30, 70, 80, 120]

common = find_common(list1, list2, list3)
print(common)

def IntersecOfSets(arr1, arr2, arr3):
	common = list(filter(lambda x: x in arr2 and x in arr3, arr1))
	print(common)

arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

IntersecOfSets(arr1, arr2, arr3)

def IntersecOfSets(arr1, arr2, arr3):
	result = []
	for i in arr1:
		if i in arr2 and i in arr3:
			result.append(i)
	print(list(set(result)))
	
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

common = IntersecOfSets(arr1, arr2, arr3)

def find_common(list1, list2, list3):
	common = set()
	for elem in list1:
		if elem in list2 and elem in list3:
			common.add(elem)
	return common

list1 = [1, 5, 10, 20, 40, 80]
list2 = [6, 7, 20, 80, 100]
list3 = [3, 4, 15, 20, 30, 70, 80, 120]

common = find_common(list1, list2, list3)
print(common)    
'''
