# Python3 code to remove after substring in string using index() + len() + slicing
str1 = 'geeksforgeeks is best for geeks'
sub_str = 'best'

res = str1[:str1.index(sub_str) + len(sub_str)]

print('The string after removal:', res)
