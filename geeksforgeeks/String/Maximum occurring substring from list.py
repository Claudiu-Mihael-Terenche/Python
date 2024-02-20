import re
import itertools
import collections
str1 = 'gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb'
list1 = ['gfg', 'is', 'best']

res1 = []
for i in list1:
	res1.append(str1.count(i))
x = max(res1)
res1 = list1[res1.index(x)]

res2 = []
for i in list1:
	import operator
	res2.append(operator.countOf(str1, i))
x = max(res2)
res2 = list1[res2.index(x)]

seqs = re.findall(str.join('|', list1), str1)

res3 = collections.Counter(seqs).most_common(1)[0][0]

groups = [(key, len(list(j))) for key, j in itertools.groupby(seqs)]

res4 = max(groups, key=lambda ele: ele[1])

count_dict = {}
for sub in list1:
	count_dict[sub] = str1.count(sub)
res5 = max(count_dict, key=count_dict.get)

max_count = 0
res6 = ''
for sub in list1:
	for substring in itertools.product(*[sub]*len(sub)):
		count = str1.count(''.join(substring))
		if count > max_count:
			max_count = count
			res6 = ''.join(substring)


print('Maximum frequency substring:\n', res1, '\n', res2, '\n', res3, '\n', res4[0], '\n', res5, '\n', res6)

'''
# Python3 code to demonstrate working of
# Maximum occurring Substring from list
# Using regex() + groupby() + max() + lambda
import re
import itertools

str1 = 'gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb'

list1 = ['gfg', 'is', 'best']

# printing original string and list
# print("The original string is : " + test_str)
# print("The original list is : " + str(test_list))

# Maximum occurring Substring from list
# Using regex() + groupby() + max() + lambda

seqs = re.findall(str.join('|', list1), str1)

groups = [(key, len(list(j))) for key, j in itertools.groupby(seqs)]

res1 = max(groups, key=lambda ele: ele[1])

print('Maximum frequency substring:', res1[0])

# Method 2: Using count() and max() methods
# Python3 code to demonstrate working of
# Maximum occurring Substring from list

# test_str = "gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb"
# test_list = ['gfg', 'is', 'best']

# printing original string and list
# print("The original string is : " + test_str)
# print("The original list is : " + str(test_list))

res2 = []
for i in list1:
	res2.append(str1.count(i))
x = max(res2)
res2 = list1[res2.index(x)]

print('Maximum frequency substring:', res2)

# Python3 code to demonstrate working of
# Maximum occurring Substring from list
# Using re.findall() + Counter
import collections
import re

# test_str = "gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb"
# test_list = ['gfg', 'is', 'best']

# printing original string and list
# print("The original string is : " + test_str)
# print("The original list is : " + str(test_list))

# Maximum occurring Substring from list
# Using re.findall() + Counter

seqs = re.findall(str.join('|', list1), str1)

res3 = collections.Counter(seqs).most_common(1)[0][0]

print('Maximum frequency substring:', res3)

# Method 4 : Using operator.countOf() and max() methods
# Python3 code to demonstrate working of
# Maximum occurring Substring from list

# test_str = "gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb"
# test_list = ['gfg', 'is', 'best']

# printing original string and list
# print("The original string is : " + test_str)
# print("The original list is : " + str(test_list))

res4 = []
for i in list1:
	import operator
	res4.append(operator.countOf(str1, i))
x = max(res4)
res4 = list1[res4.index(x)]

print('Maximum frequency substring:', res4)

# Python3 code to demonstrate working of
# Maximum occurring Substring from list
# Using dictionary

# test_str = "gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb"
# test_list = ['gfg', 'is', 'best']

# printing original string and list
# print("The original string is : " + test_str)
# print("The original list is : " + str(test_list))

# Maximum occurring Substring from list
# Using dictionary

count_dict = {}
for sub in list1:
	count_dict[sub] = str1.count(sub)
res5 = max(count_dict, key=count_dict.get)

print('Maximum frequency substring:', res5)

# Python3 code to demonstrate working of
# Maximum occurring Substring from list
# Using itertools.product() and count()
import itertools

# test_str = "gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb"
# test_list = ['gfg', 'is', 'best']

# printing original string and list
# print("The original string is : " + test_str)
# print("The original list is : " + str(test_list))

# Maximum occurring Substring from list
# Using itertools.product() and count()

max_count = 0
max_substring = ""
for sub in list1:
	for substring in itertools.product(*[sub]*len(sub)):
		count = str1.count(''.join(substring))
		if count > max_count:
			max_count = count
			max_substring = ''.join(substring)


print('Maximum frequency substring:', max_substring)
'''
