from collections import Counter
tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)

res = dict(Counter(tup))

print('Tuple elements frequency is:', res)

'''
# Python3 code to check elements frequency in tuple using Counter()
from collections import Counter

tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)

# printing original tuple
# print("The original tuple is : " + str(tup))

# converting result back from defaultdict to dict

res = dict(Counter(tup))

print('Tuple elements frequency is:', res)
'''
