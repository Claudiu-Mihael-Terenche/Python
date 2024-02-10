list1 = [(5, 6, 7), (1, 3, 5), (8, 9, 19)]

K = 2

prod = 1
for tup in list1: prod *= tup[K]

print('Product of Kth column of tuple list:', prod)
