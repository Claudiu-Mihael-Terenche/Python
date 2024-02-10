# Python3 code for suffix removal from string list using loop + remove() + endswith()

list = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']

suff = 'x'

for word in list[:]:
	if word.endswith(suff):
		list.remove(word)

print('List after removal of suffix elements:', list)

'''
# Python3 code to demonstrate working of
# Suffix removal from String list
# using list comprehension + endswith()

# initialize list 
test_list = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']

# printing original list 
print("The original list : " + str(test_list))

# initialize suff
suff = 'x'

# Suffix removal from String list
# using list comprehension + endswith()
res = [ele for ele in test_list if not ele.endswith(suff)]

# printing result
print("List after removal of suffix elements : "+ str(res))

# Python3 code to demonstrate working of
# Remove prefix strings from list
# using filter + endswith()

# initialize suff
suff = 'x'

def eva(x):
	return not x.endswith(suff)
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
suff = "x"

res = []
# Suffix removal from String list
for i in test_list:
	if(i[-1] != suff):
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
suff = "x"

res = []
# Suffix removal from String list
for i in test_list:
	if(i.find(suff)!=len(i)-1):
		res.append(i)

# printing result
print("List after removal of suffix elements : " + str(res))

# Python3 code to demonstrate working of
# Remove prefix strings from list using lambda functions

# initialize suff
suff = 'x'

# initialize list
test_list = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']

# printing original list
print("The original list : " + str(test_list))

# Remove prefix strings from list

res = list(filter(lambda x: x[-1] != suff, test_list))

# printing result
print("List after removal of Kth character of each string : " + str(res))

# Using regular expressions
import re

# initialize list
test_list = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']

# printing original list
print("The original list : " + str(test_list))

# initialize suffix
suff = 'x$'

# Suffix removal from String list using regular expressions
res = [x for x in test_list if not re.search(suff, x)]

# printing result
print("List after removal of suffix elements : " + str(res))
#This code is contributed by Edula Vinay Kumar Reddy
'''
