# Using list comprehension and set intersection

list1 = [[1, 2], [3, 4], [5, 6]]; list2 = [[3, 4], [5, 7], [1, 2]]

res = [x for x in list1 if x not in list2] + [y for y in list2 if y not in list1]

print('The uncommon of two lists is:', res)
