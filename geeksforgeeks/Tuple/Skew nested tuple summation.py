tup = (5, (6, (1, (9, (10, None)))))

res = 0
while tup:
    res += tup[0]
    tup = tup[1]

print('Summation of 1st positions:', res)

'''
# Python3 code to demonstrate working of
# Skew Nested Tuple Summation #
# sing infinite loop

tup = (5, (6, (1, (9, (10, None)))))

# printing original tuple
# print("The original tuple is : " + str(test_tup))

res = 0
while tup:
    res += tup[0]
    tup = tup[1] # assigning inner tuple as original

print('Summation of 1st positions:', res)
'''
