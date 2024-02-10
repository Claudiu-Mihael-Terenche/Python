import re

str1 = 'gfggfggfggfggfggfggfggfg'

K = 'gfg'

res1 = re.findall(K, str1)

re = str1.count(K)
res2 = [K]*re

temp = len(str1) // len(str(K))
res3 = [K] * temp

# printing result
print('The split string is:\n',  res1, '\n', res2, '\n', res3)

'''
# Python3 code to split by repeating substring using re.findall()
import re

# initializing string
str1 = 'gfggfggfggfggfggfggfggfg'

# printing original string
# print("The original string is : " + str1)

# initializing target
K = 'gfg'

# split by repeating substring using re.findall()
res = re.findall(K, str1)

# printing result
print('The split string is:', str(res))

# Using count() method and * operator
# Python3 code to demonstrate working of
# Split by repeating substring

# initializing string
test_str = "gfggfggfggfggfggfggfggfg"

# printing original string
print("The original string is : " + test_str)

# initializing target
K = 'gfg'

# Split by repeating substring
re=test_str.count(K)
res=[K]*re

# printing result
print("The split string is : " + str(res))

# Python3 code to demonstrate working of
# Split by repeating substring
# Using * operator + len()

# initializing string
test_str = "gfggfggfggfggfggfggfggfg"

# printing original string
print("The original string is : " + test_str)

# initializing target
K = 'gfg'

# Split by repeating substring
# Using * operator + len()
temp = len(test_str) // len(str(K))
res = [K] * temp

# printing result
print("The split string is : " + str(res))
'''
