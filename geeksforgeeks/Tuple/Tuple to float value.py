tup = (4, 56)

res1 = float('{}.{}'.format(*tup))

res2 = float('.'.join(str(ele) for ele in tup))

print('The float after conversion from tuple is:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Convert tuple to float
# using format() + join()

tup = (4, 56)

# printing original tuple
# print("The original tuple : " + str(test_tup))

# Convert tuple to float
# using format() + join()

res1 = float('{}.{}'.format(*tup))

# print('The float after conversion from tuple is:', res1)

# Python3 code to demonstrate working of
# Convert tuple to float
# using join() + float() + str() + generator expression

# initialize tuple
# tup = (4, 56)

# printing original tuple
# print("The original tuple : " + str(test_tup))

# Convert tuple to float
# using join() + float() + str() + generator expression

res2 = float('.'.join(str(ele) for ele in tup))

print('The float after conversion from tuple is:\n', res1, '\n', res2)
'''
