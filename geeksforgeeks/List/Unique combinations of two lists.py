import itertools
from itertools import product
list1 = ['b', 'c', 'd']
list2 = [1, 4, 9]

res1 = list(list(zip(list1, item)) for item in product(list2, repeat=len(list1)))

res2 = []

permute = itertools.permutations(list1, len(list2))

for comb in permute:
    zipped = zip(comb, list2)
    res2.append(list(zipped))

print('', res1, '\n', res2)

'''
from itertools import permutations
# Python program for unique combination of two lists using zip() and product() of itertools

# import itertools package
import itertools
from itertools import product

list1 = ['b', 'c', 'd']
list2 = [1, 4, 9]

unique_combinations = [] # create empty list to store the combinations

# extract combination mapping in two lists using zip() + product()
unique_combinations1 = list(list(zip(list1, item)) for item in product(list2, repeat = len(list1)))

print(unique_combinations1)

# Version 2: Python program for unique combination of two lists using zip() and permutation of itertools

# import itertools package
import itertools
from itertools import permutations
# list1_2 = ["a", "b", "c","d"]
# list2_2 = [1,4,9]

# create empty list to store the combinations

unique_combinations2 = []

permute = itertools.permutations(list1, len(list2)) # getting all permutations of list1 with length of list2

# zip() is called to pair each permutation and shorter list element into combination
for comb in permute:
zipped = zip(comb, list2)
unique_combinations2.append(list(zipped))

print(unique_combinations2)
'''
