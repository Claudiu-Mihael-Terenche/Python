file = open('gfg input file.txt')

content = file.readlines()

res1 = content[1]

print('Second line:\n', res1)

res2 = content[0:3]

print('First 3 lines:\n', *res2)

import linecache

res3 = linecache.getline('gfg input file.txt', 2)

print('Second line:\n', res3)

'''
# Using fileobject.readlines() open the sample file used

file = open('gfg input file.txt')

content = file.readlines() # read the content of the file opened

res1 = content[1]

print('Second line:\n', res1) # read 2nd line from the file

res2 = content[0:3]

print('First 3 lines:\n', *res2) # print first 3 lines of file

# Using linecache package
# importing required package
import linecache

res3 = linecache.getline('gfg input file.txt', 2) # extracting the 2nd line

print('Second line:\n', res3)
'''
