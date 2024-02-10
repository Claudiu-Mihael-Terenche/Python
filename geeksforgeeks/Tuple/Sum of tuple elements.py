import math

tup1 = (7, 8, 9, 1, 10, 7)

res1 = math.fsum(tup1)

ele = [item for item in tup1]

res2 = sum(ele)

print('\r', res1, '\n', res2)

tup3 = ([7, 8], [9, 1], [10, 7])

res3 = sum(list(map(sum, list(tup3))))

print('The summation of tuple elements are:', res3)

tup41 = (1, 2, 3)
tup42 = (4, 5, 6)
tup43 = (7, 8, 9)

combined = zip(tup41, tup42, tup43)

res4 = tuple(map(sum, combined))

print(res4)

'''
# Using math library
import math

tup1 = (7, 8, 9, 1, 10, 7)

res1 = math.fsum(tup1) # calculating sum of tuple elements using math.fsum()

# print('The summation of tuple elements are:', res1)

# Using list comprehension

# def summation(tup1):
    # ele = [item for item in tup1] # convert the tuple to a list using a list comprehension
    # return sum(ele) # find the sum of the elements in the list using the built-in sum() function

# tup1 = (5, 20, 3, 7, 6, 8)

# print(summation(tup1))

# tup1 = (5, 20, 3, 7, 6, 8)

ele = [item for item in tup1]

res2 = sum(ele)

print('\r', res1, '\n', res2)

# Python 3 code to do Tuple elements inversions using map() + list() + sum()

tup3 = ([7, 8], [9, 1], [10, 7])

# printing original tuple
# print("The original tuple is : " + str(tup2))

# Tuple elements inversions using map() + list() + sum()

res3 = sum(list(map(sum, list(tup3))))

print('The summation of tuple elements are:', res3)

# Using zip() function
tup41 = (1, 2, 3)
tup42 = (4, 5, 6)
tup43 = (7, 8, 9)

combined = zip(tup41, tup42, tup43)

res4 = tuple(map(sum, combined))

print(res4)
'''
