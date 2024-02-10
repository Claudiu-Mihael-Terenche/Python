from collections import OrderedDict

ar1 = [1, 5, 10, 20, 40, 80]; ar2 = [6, 7, 20, 80, 100]; ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

lst = []

dict1 = OrderedDict.fromkeys(ar1); dict2 = OrderedDict.fromkeys(ar2); dict3 = OrderedDict.fromkeys(ar3)

for values1, keys1 in dict1.items():
	for values2, keys2 in dict2.items():
		for values3, keys3 in dict3.items():
			if values1 == values2 == values3:
				lst.append(values1)

print('Common elements:', *lst)
