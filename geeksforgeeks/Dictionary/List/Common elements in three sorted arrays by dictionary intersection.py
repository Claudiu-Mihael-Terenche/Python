from collections import OrderedDict
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

list1 = []

dict1 = OrderedDict.fromkeys(ar1)
dict2 = OrderedDict.fromkeys(ar2)
dict3 = OrderedDict.fromkeys(ar3)

for vals1, keys1 in dict1.items():
	for vals2, keys2 in dict2.items():
		for vals3, keys3 in dict3.items():
			if vals1 == vals2 == vals3:
				list1.append(vals1)

print('Common elements:', *list1)
