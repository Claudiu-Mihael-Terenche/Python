# Python program to print all the possible combinations using itertools.permutations()

from itertools import permutations

comb = permutations([1, 2, 3], 3) # get all combination of [1, 2, 3] of length 3

for num in comb: print(num)
