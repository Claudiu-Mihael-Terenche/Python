str1 = 'geeksforgeeks'

K = 'seek'

def temp(sub): return ''.join(chr for chr in sub if chr in set(K))

res1 = K in temp(str1)

str1 = iter(str1)

res2 = all(next((ele for ele in str1 if ele == chr), None) is not None for chr in K)

print('Is substring in order:\n', res1, '\n', res2)

'''
# Python3 code to test substring order using join() + in operator + generator expression

# initializing string
str1 = 'geeksforgeeks'

# printing original string
# print("The original string is : " + str(str1))

# initializing substring
K1 = 'seek'

# concatenating required characters

def temp(sub): return ''.join(chr for chr in sub if chr in set(K1))


# checking in order
res1 = K1 in temp(str1)

# printing result
print('Is substring in order:', str(res1))

# Python3 code to demonstrate working of test substring order using all() + next() + generator expression

# initializing string
str2 = 'geeksforgeeks'

# printing original string
# print("The original string is : " + str(str2))

# initializing substring
K2 = 'seek'

# concatenating required characters using next()
# all() used to test order
str2 = iter(str2)
res2 = all(next((ele for ele in str2 if ele == chr), None) is not None for chr in K2)

# printing result
print('Is substring in order:', str(res2))
'''
