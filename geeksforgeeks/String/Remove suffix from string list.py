# Python3 code for suffix removal from a string list using loop + remove() + endswith()
list1 = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']
suffix = 'x'

for word in list1[:]:
	if word.endswith(suffix):
		list1.remove(word)

print('List after removal of suffix elements:', list1)

'''
# Python3 code to demonstrate working of
# Suffix removal from String list
# using list comprehension + endswith()

# initialize list 
test_list = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']

# printing original list 
print("The original list : " + str(test_list))

# initialize suffix
suffix = 'x'

# Suffix removal from String list
# using list comprehension + endswith()
res = [ele for ele in test_list if not ele.endswith(suffix)]

# printing result
print("List after removal of suffix elements : "+ str(res))

# Python3 code to demonstrate working of
# Remove prefix strings from list
# using filter + endswith()

# initialize suffix
suffix = 'x'

def eva(x):
	return not x.endswith(suffix)
# initialize list 
test_list = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']

# printing original list 
print("The original list : " + str(test_list))

# Remove prefix strings from list
# using filter + endswith()
res = list(filter(eva, test_list))

# printing result
print("List after removal of Kth character of each string : " + str(res))

# Python3 code to demonstrate working of
# Suffix removal from String list

# initialize list
test_list = ["allx", "lovex", "gfg", "xit", "is", "bestx"]

# printing original list
print("The original list : " + str(test_list))

# initialize suffix
suffix = "x"

res = []
# Suffix removal from String list
for i in test_list:
	if(i[-1] != suffix):
		res.append(i)

# printing result
print("List after removal of suffix elements : " + str(res))

# Python3 code to demonstrate working of
# Suffix removal from String list using find() and len() methods

# initialize list
test_list = ["allx", "lovex", "gfg", "xit", "is", "bestx"]

# printing original list
print("The original list : " + str(test_list))

# initialize suffix
suffix = "x"

res = []
# Suffix removal from String list
for i in test_list:
	if(i.find(suffix)!=len(i)-1):
		res.append(i)

# printing result
print("List after removal of suffix elements : " + str(res))

# Python3 code to demonstrate working of
# Remove prefix strings from list using lambda functions

# initialize suffix
suffix = 'x'

# initialize list
test_list = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']

# printing original list
print("The original list : " + str(test_list))

# Remove prefix strings from list

res = list(filter(lambda x: x[-1] != suffix, test_list))

# printing result
print("List after removal of Kth character of each string : " + str(res))

# Using regular expressions
import re

# initialize list
test_list = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']

# printing original list
print("The original list : " + str(test_list))

# initialize suffix
suffix = 'x$'

# Suffix removal from String list using regular expressions
res = [x for x in test_list if not re.search(suffix, x)]

# printing result
print("List after removal of suffix elements : " + str(res))
'''
