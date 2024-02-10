'''
set.remove()
set.clear()
set.union()
set.intersection()
set.difference()
set.symmetric_difference()
set.issubset()
set.issuperset()

set.pop()
set.update()
set.add()
set.discard()

Set Methods
Function	Description
add()	Adds an element to a set
remove()	Removes an element from a set. If the element is not present in the set, raise a KeyError
clear()	Removes all elements form a set
copy()	Returns a shallow copy of a set
pop()	Removes and returns an arbitrary set element. Raise KeyError if the set is empty
update()	Updates a set with the union of itself and others
union()	Returns the union of sets in a new set
difference()	Returns the difference of two or more sets as a new set
difference_update()	Removes all elements of another set from this set
discard()	Removes an element from set if it is a member. (Do nothing if the element is not in set)
intersection()	Returns the intersection of two sets as a new set
intersection_update()	Updates the set with the intersection of itself and another
isdisjoint()	Returns True if two sets have a null intersection
issubset()	Returns True if another set contains this set
issuperset()	Returns True if this set contains another set
symmetric_difference()	Returns the symmetric difference of two sets as a new set
symmetric_difference_update()	Updates a set with the symmetric difference of itself and another

# Python program to illustrate a set

# define a set and its elements
myset = set(['geeks', 'for', 'geeks'])

#as set doesn't have duplicate elements so, 1 geeks will not be printed
print(myset)
'''

set1 = {1, 2, 3, 4, 5}
for i in range(1, 6): set1.add(i)
print(set1)

set2 = {1, 2, 3, 4, 5}
for i in set2: print(i, end=' ')

print('\r')

set3 = {1, 2, 3, 4, 5}
for i in range(1, 5): set3.remove(i)
print(set3)

def create_set():
	set4 = {1, 2, 3, 4, 5}
	print(set4)

def add_element():
	set5 = {1, 2, 3, 4, 5}
	set5.add(6)
	print(set5)

def remove_element():
	set6 = {1, 2, 3, 4, 5}
	set6.remove(3)
	print(set6)

def clear_set():
	set7 = {1, 2, 3, 4, 5}
	set7.clear()
	print(set7)

def set_union():
	set81 = {1, 2, 3}
	set82 = {4, 5, 6}
	set83 = set81.union(set82)
	print(set83)

def set_intersection():
	set91 = {1, 2, 3, 4, 5}
	set92 = {4, 5, 6, 7, 8}
	set93 = set91.intersection(set92)
	print(set93)

def set_difference():
	set101 = {1, 2, 3, 4, 5}
	set102 = {4, 5, 6, 7, 8}
	set103 = set101.difference(set102)
	print(set103)

def set_symmetric_difference():
	set111 = {1, 2, 3, 4, 5}
	set112 = {4, 5, 6, 7, 8}
	set113 = set111.symmetric_difference(set112)
	print(set113)

def set_subset():
	set121 = {1, 2, 3, 4, 5}
	set122 = {2, 3, 4}
	subset = set122.issubset(set121)
	print(subset)

def set_superset():
	set131 = {1, 2, 3, 4, 5}
	set132 = {2, 3, 4}
	superset = set131.issuperset(set132)
	print(superset)

if __name__ == '__main__':
	create_set()
	add_element()
	remove_element()
	clear_set()
	set_union()
	set_intersection()
	set_difference()
	set_symmetric_difference()
	set_subset()
	set_superset()
