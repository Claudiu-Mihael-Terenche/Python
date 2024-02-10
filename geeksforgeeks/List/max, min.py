a = 2; b = 4

max1 = max(a, b)
min1 = min(a, b)

max2 = a if a >= b else b
min2 = a if a <= b else b

max3 = sorted([a, b])[-1]
min3 = sorted([a, b])[0]

list4 = [a, b]
list4.sort()

max4 = list4[-1]
min4 = list4[0]

print('Max:', max1, max2, max3, max4, '\nMin:', min1, min2, min3, min4)

'''
# Python program to find the maximum (minimum) of two numbers

a = 2; b = 4

max1 = max(a, b)
min1 = min(a, b)

# print('Max:', max1, '\nMin:', min1)

# Version 2: using ternary operator

# driver code

# a2 = 2; b2 = 4

# use of ternary operator

max2 = a if a >= b else b
min2 = a if a <= b else b

# print('Max:', max2, '\nMin:', min2)

# reverse signs for min

# Version 3: using sort method

# a3 = 2; b3 = 4

max3 = sorted([a, b])[-1]
min3 = sorted([a, b])[0]

# print('Max:', max3, '\nMin:', min3)

# Version 4
# a4 = 2; b4 = 4

list4 = [a, b]
list4.sort()

max4 = list4[-1]
min4 = list4[0]

print('Max:', max1, max2, max3, max4, '\nMin:', min1, min2, min3, min4)
'''
