# Python3 code replace index elements with elements in other list using list comprehension
list1 = ['Gfg', 'is', 'best']
list2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]

res = [list1[idx] for idx in list2]

print('The lists after index elements replacements is:', res)
