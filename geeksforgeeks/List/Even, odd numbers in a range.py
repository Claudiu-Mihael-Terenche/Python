start = 4
end = 15

even_nums1 = [num for num in range(start, end + 1) if num % 2 == 0]
odd_nums1 = [num for num in range(start, end + 1) if num % 2 != 0]

print('Even nums:', *even_nums1, '\nOdd nums:', *odd_nums1)

for even_nums2 in range(start, end + 1, 2):
    print(even_nums2, end=' ')

print('\r')

for odd_nums2 in range(start, end + 1):
    if odd_nums2 % 2 != 0:
        print(odd_nums2, end=' ')

'''
# Using list comprehension

start = 4; end = 15

even_nums1 = [num for num in range(start, end + 1) if num % 2 == 0]
odd_nums1 = [num for num in range(start, end + 1) if num % 2 != 0]

print('Even nums:', *even_nums1, '\nOdd nums:', *odd_nums1)

# Version 2: Python program to print all even numbers in range using for loop
# start = 4; end = 15

# here inside range function first no denotes starting, second denotes end and third denotes the interval

for even_nums2 in range(start, end + 1, 2):
    print(even_nums2, end=' ')

print('\r')

# Version 3: Python program to print odd numbers in a given range using for loop

# start, end = 4, 15

# iterating each number in list

for odd_nums2 in range(start, end + 1):
    if odd_nums2 % 2 != 0:
        print(odd_nums2, end=' ')
'''
