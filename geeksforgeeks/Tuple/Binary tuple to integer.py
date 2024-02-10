tup = (1, 1, 0, 1, 0, 0, 1)

res = int(''.join(str(ele) for ele in tup), 2)

print('Decimal number is:', res)

'''
# Python3 code to convert binary tuple to integer using join() + list comprehension + int()

tup = (1, 1, 0, 1, 0, 0, 1)

# printing original tuple
# print("The original tuple is : " + str(test_tup))

# using int() with base to get actual number

res = int(''.join(str(ele) for ele in tup), 2)

print('Decimal number is:', res)
'''
