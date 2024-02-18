from collections import Counter
str1 = 'ABHISHEKsinGH'
str2 = 'gfhfBHkooIHnfndSHEKsiAnG'

dict1 = Counter(str1)
dict2 = Counter(str2)

res1 = dict1 & dict2

res2 = res1 == dict1

print(res2)

'''
# Python code to find if we can make first string
# from second by deleting some characters from
# second and rearranging remaining characters.
from collections import Counter

def makeString(str1,str2):

# convert both strings into dictionaries
# output will be like str1="aabbcc",
# dict1={'a':2,'b':2,'c':2}
# str2 = 'abbbcc', dict2={'a':1,'b':3,'c':2}
dict1 = Counter(str1); dict2 = Counter(str2)

# take intersection of two dictionaries
# output will be result = {'a':1,'b':2,'c':2}
res = dict1 & dict2

# compare resultant dictionary with first
# dictionary comparison first compares keys
# and then compares their corresponding values
return res == dict1

# driver program
if __name__ == '__main__':

str1 = 'ABHISHEKsinGH'
str2 = 'gfhfBHkooIHnfndSHEKsiAnG'

if (makeString(str1,str2)==True):
print('Possible')
else:
print('Not possible')
'''
