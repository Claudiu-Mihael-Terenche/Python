from collections import defaultdict

list1 = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]

res1 = []
for sub in list1:
	if res1 and res1[-1][0] == sub[0]:
		res1[-1].extend(sub[1:])
	else:
		res1.append([ele for ele in sub])
res1 = list(map(tuple, res1))

mapp = defaultdict(list)
for key, val in list1:
	mapp[key].append(val)
res2 = [(key, *val) for key, val in mapp.items()]

temp_dict = {}
for x in list1: temp_dict[x[0]] = temp_dict.get(x[0], []) + list(x[1:])

res3 = [(k,) + tuple(v) for k, v in temp_dict.items()]

from itertools import groupby

res4 = []
for k, g in groupby(list1, key=lambda x: x[0]):
	values = [v for _, v in g]
	res4.append((k, *values))

def join_tuples(list1, index):
	if index == len(list1) - 1:
		return list1
	elif list1[index][0] == list1[index + 1][0]:
		list1[index] += list1[index + 1][1:]
		list1.pop(index + 1)
		return join_tuples(list1, index)
	else:
		return join_tuples(list1, index + 1)


res5 = join_tuples(list1, 0)

print('The extracted elements:\n', res1, '\n', res2, '\n', res3, '\n', res4, '\n', res5)

'''
# Python3 code to join tuples if similar initial element using loop

list1 = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]

# printing original list
# print("The original list is : " + str(list1))

# join tuples if similar initial element using loop

res1 = []
for sub in list1:
	if res1 and res1[-1][0] == sub[0]:
		res1[-1].extend(sub[1:])
	else:
		res1.append([ele for ele in sub])
res1 = list(map(tuple, res1))

# print('The extracted elements:', res1)

# Python3 code to join tuples if similar initial element using defaultdict() + loop
from collections import defaultdict

# list2 = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]

# printing original list
# print("The original list is : " + str(list2))

# join tuples if similar initial element using defaultdict() + loop

mapp = defaultdict(list)
for key, val in list1:
	mapp[key].append(val)
res2 = [(key, *val) for key, val in mapp.items()]

# print('The extracted elements:', res2)

# Using dictionary and list comprehension

# list3 = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]

# printing original list
# print("The original list is : " + str(list3))

# join tuples if similar initial element using dictionary and list comprehension

temp_dict = {}
for x in list1: temp_dict[x[0]] = temp_dict.get(x[0], []) + list(x[1:])

res3 = [(k,) + tuple(v) for k, v in temp_dict.items()]

# print('The extracted elements:', res3)

# Using itertools.groupby()
from itertools import groupby

# list4 = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]

# printing original list
# print("The original list is : " + str(list4))

# join tuples if similar initial element using itertools.groupby()

res4 = []
for k, g in groupby(list1, key=lambda x: x[0]):
	values = [v for _, v in g]
	res4.append((k, *values))

# print('The extracted elements:', res4)

# Python3 code to join tuples if similar initial element using recursion

def join_tuples(list1, index):
	if index == len(list1) - 1:
		return list1
	elif list1[index][0] == list1[index + 1][0]:
		list1[index] += list1[index + 1][1:]
		list1.pop(index + 1)
		return join_tuples(list1, index)
	else:
		return join_tuples(list1, index + 1)


# list5 = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]

# printing original list
# print("The original list is : " + str(list5))

# join tuples if similar initial element using recursion

res5 = join_tuples(list1, 0)

print('The extracted elements:\n', res1, '\n', res2, '\n', res3, '\n', res4, '\n', res5)
'''
