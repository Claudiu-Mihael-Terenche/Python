'''
List Methods
Function	Description
Append()	Add an element to the end of the list
Extend()	Add all elements of a list to another list
Insert()	Insert an item at the defined index
Remove()	Removes an item from the list
Clear()	Removes all items from the list
Index()	Returns the index of the first matched item
Count()	Returns the count of the number of items passed as an argument
Sort()	Sort items in a list in ascending order
Reverse()	Reverse the order of items in the list
copy()	Returns a copy of the list
pop()	Removes and returns the item at the specified index. If no index is provided, it removes and returns
                                                                                               the last item.
To know more refer to this article – Python List methods

The operations mentioned above modify the list Itself.

Built-in functions with List
Function	Description
reduce()	apply a particular function passed in its argument to all of the list elements stores
                               the intermediate result and only returns the final summation value
sum()	Sums up the numbers in the list
ord()	Returns an integer representing the Unicode code point of the given Unicode character
cmp()	This function returns 1 if the first list is “greater” than the second list
max()	return maximum element of a given list
min()	return minimum element of a given list
all()	Returns true if all element is true or if the list is empty
any()	return true if any element of the list is true. if the list is empty, return false
len()	Returns length of the list or size of the list
enumerate()	Returns enumerate object of the list
accumulate()	apply a particular function passed in its argument to all of the list elements
                                            returns a list containing the intermediate results
filter()	tests if each element of a list is true or not
map()	returns a list of the results after applying the given function to each item of a given iterable
lambda()	This function can have any number of arguments but only one expression, which is evaluated
                                                                                          and returned.

import math
import copy

list1.index(item) # position of the item
list1.extend(multiple) # append multiple
list1.append(item) # append item to a list
list1.append(list2) # append list to a list
list1.insert(position, value) # insert to a list
list1.pop(item) # remove an item
list1.clear() # clear list
list1.reverse() # reverse list
list1.set(list1) # remove duplicates
list1.remove([]) # remove empty list from list
list1.remove(item) # remove item from list
list(filter(None, list1)) # remove empty list from list

# iteration by for loop on list
list1 = [1, 4, 5, 7, 8, 9]
for num in list1:
	print(num)

# store integers in a list using map, split and strip functions
list1 = list(map(int, input('Enter the integer\elements:').strip().split()))[:n]

# printing the list
print('The list is:', list1)

*list1 # unpacking list into args

copy.copy(list1) # copy list with import copy

[item for item in list1 if item != []] # remove empty list from list
[num for num in list1 if num % 2 == 0] # even nums, len for count
[num for num in list1 if num % 2 != 0] # odd nums, len for count
[num for num in list1 if num > 0] # pos nums, len for count
[num for num in list1 if num < 0] # neg nums, len for count
[num for num in list1 if num in wanted_num] # removing nums from list, wanted_num = {a, b}
[num for num in list1 if num not in unwanted_num] # removing nums from list, unwanted_num = {a, b}
[num for num in range(a, b + 1) if num % 2 != 0] # odd nums in a range
[num for num in range(a, b + 1) if num % 2 == 0] # even nums in a range
[num for num in range(a, b + 1) if num > 0] # pos nums in a range
[num for num in range(a, b + 1) if num < 0] # neg nums in a range
[j for i, j in enumerate(list) if j != item] # remove all occurences of an element
[list1[i] for i in list2] # replace index elements with elements in other list
[i[::-1] for i in list1] # reverse strings in string list
[item for temp in list1 for item in temp.split() if item[0].lower() == K.lower()] # extract words starting with
                                                                                            # K in strings list

del list1[a:b] # removing nums between a and b

len(list1) # length of list
max(list1) # biggest num
min(list1) # smallest num
sum(list1) # sum of the nums
math.prod(list1) # multiply nums
''.join(chain(*list1)) # convert character matrix to a single string

comb = permutations([1, 2, 3], 3) # combinations of 3
'''
