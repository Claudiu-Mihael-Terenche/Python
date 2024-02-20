# Python3 code to check if string is subset of another using issubset()
str1 = 'geeksforgeeks'
str2 = 'gfks'

res1 = set(str2).issubset(str1)

res2 = all(ele in str1 for ele in str2)

print('Does string contains all the characters of other list?:\n', res1, '\n', res2)
