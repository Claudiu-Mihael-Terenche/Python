from itertools import combinations

list1 = ['GFG', [5, 4], 'is', ['best', 'good', 'better', 'average']]

idx = 0

temp = combinations(list1, 2)

for item in list(temp):
	idx = idx + 1
	print('Combination', idx, ':', item)
