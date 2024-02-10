# Python3 code to find word location in string using split() and index() methods

str1 = 'geeksforgeeks is best for geeks'

word = 'best'

res = str1.split().index(word) + 1

print('The location of word is:', res)
