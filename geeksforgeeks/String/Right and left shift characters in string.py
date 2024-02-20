str1 = 'geeksforgeeks'

r_rot = 7
l_rot = 3

temp = (r_rot - l_rot) % len(str1)

res1 = str1[temp:] + str1[:temp]

res2 = (str1 * 3)[len(str1) + r_rot - l_rot: 2 * len(str1) + r_rot - l_rot]

print('The string after rotation is:\n', res1, '\n', res2)

'''
# Python3 code for right and left shift characters in string using % operator and string slicing

# initializing string
str1 = 'geeksforgeeks'

# printing original string
# print('The original string is:', str1)

# initializing right rot
r_rot1 = 7

# initializing left rot
l_rot1 = 3

# right and left shift characters in string using % operator and string slicing
temp = (r_rot1 - l_rot1) % len(str1)
res1 = str1[temp:] + str1[:temp]

# printing result
print('The string after rotation is:', str(res1))

# Version 2: Python3 code for right and left shift characters in string
# using string multiplication + string slicing

# Initializing string
str2 = 'geeksforgeeks'

# printing original string
# print('The original string is:', str2)

# initializing right rot
r_rot2 = 7

# initializing left rot
l_rot2 = 3

# right and left shift characters in string using string multiplication + string slicing
res2 = (str2 * 3)[len(str2) + r_rot2 - l_rot2: 2 * len(str2) + r_rot2 - l_rot2]

# printing result
print('The string after rotation is:', str(res2))
'''
