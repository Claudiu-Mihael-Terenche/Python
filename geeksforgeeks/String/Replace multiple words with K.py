# Python3 code to replace multiple words with K
str1 = 'Geeksforgeeks is best for geeks and CS'
list1 = ['best', 'CS', 'for']
word = 'gfg'

for item in list1:
    str1 = str1.replace(item, word)

print('String after multiple replace:', str1)
