from itertools import permutations

# Python3 code to filter strings combination of K substrings
# using permutations() + map() + join() + set() + intersection()

list1 = ['geeks4u', 'allbest', 'abcdef']

substr_list = ['s4u', 'est', 'al', 'ge', 'ek', 'def', 'lb']

K = 3

perms = set(map(''.join, permutations(substr_list, r = K))) # getting all permutations

res = list(set(list1).intersection(perms)) # using intersection() to solve this problem

print('Strings after joins:', res)
