'''
Built-In Methods
Built-in-Method	Description
index( )	Find in the tuple and returns the index of the given value where it’s available
count( )	Returns the frequency of occurrence of a specified value
Built-In Functions
Built-in Function	Description
all()	Returns true if all element are true or if tuple is empty
any()	return true if any element of the tuple is true. if tuple is empty, return false
len()	Returns length of the tuple or size of the tuple
enumerate()	Returns enumerate object of tuple
max()	return maximum element of given tuple
min()	return minimum element of given tuple
sum()	Sums up the numbers in the tuple
sorted()	input elements in the tuple and return a new sorted list
tuple()	Convert an iterable to a tuple.

# tuple unpacking
tuple1 = ('geeks', 'for', 'geeks')

# this line unpack values of tuple1
a, b, c = tuple1
print('\nValues after unpacking: ')
print(a)
print(b)
print(c)

tuple3 = tuple1 + tuple2 # concatinating of tuples

Tuples VS Lists:
Similarities	Differences
Functions that can be used for both lists and tuples:

len(), max(), min(), sum(), any(), all(), sorted()

Methods that cannot be used for tuples:

append(), insert(), remove(), pop(), clear(), sort(), reverse()

Methods that can be used for both lists and tuples:

count(), Index()

we generally use ‘tuples’ for heterogeneous (different) data types and ‘lists’ for homogeneous (similar) data types.
Tuples can be stored in lists.	Iterating through a ‘tuple’ is faster than in a ‘list’.
Lists can be stored in tuples.	‘Lists’ are mutable whereas ‘tuples’ are immutable.
Both ‘tuples’ and ‘lists’ can be nested.	Tuples that contain immutable elements can be used as a key for a dictionary.
'''
