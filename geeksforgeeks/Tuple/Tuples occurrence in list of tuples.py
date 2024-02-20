from collections import Counter
from itertools import chain
list1 = [[('hi', 'bye')], [('Geeks', 'forGeeks')], [('a', 'b')], [('hi', 'bye')], [('a', 'b')]]

res = Counter(chain(*list1))

print(res)

'''
# Using chain and Counter
# Python code to count unique
# tuples in list of list

from collections import Counter
from itertools import chain

list1 = [[('hi', 'bye')], [('Geeks', 'forGeeks')], [('a', 'b')], [('hi', 'bye')], [('a', 'b')]]

res = Counter(chain(*list1)) # using counter and chain

print(res)
'''
