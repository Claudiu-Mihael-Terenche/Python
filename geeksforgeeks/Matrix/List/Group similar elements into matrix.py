from itertools import groupby
# Python3 code to group similar elements into matrix using list comprehension + groupby()
list1 = [1, 3, 5, 1, 3, 2, 5, 4, 2]

res = [list(val) for key, val in groupby(sorted(list1))]

print('Matrix after grouping:', res)
