list1 = [10, 15, 20, 25, 30, 35, 40]; list2 = [25, 40, 35]

set1 = set(list1)
set2 = set(list2)

res1 = sorted(list(set1 - set2))

print(res1)

res2 = [x for x in list1 if x not in set2]

print(res2)

res3 = []
for element in list1:
	if element not in list2:
		res3.append(element)

print(res3)

'''
# Using list comprehension

list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]

set1 = set(list1)
set2 = set(list2)

res1 = sorted(list(set1 - set2))

print(res1)

# set2 = set(list2)
res2 = [x for x in list1 if x not in set2]

print(res2)

# li1 = [10, 15, 20, 25, 30, 35, 40]
# li2 = [25, 40, 35]

res3 = []
for element in list1:
	if element not in list2:
		res3.append(element)

print(res3)
'''
