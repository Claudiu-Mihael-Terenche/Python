from collections import Counter

def checkAnagram(num1, num2):

    bin1 = bin(num1)[2:]
    bin2 = bin(num2)[2:]
    zeros = abs(len(bin1) - len(bin2))

    if (len(bin1) > len(bin2)):
        bin2 = zeros * '0' + bin2
    else:
        bin1 = zeros * '0' + bin1


    dict1 = Counter(bin1); dict2 = Counter(bin2)

    if dict1 == dict2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    num1 = 8; num2 = 4
    checkAnagram(num1, num2)

def is_anagram_binary(a, b):

	bin_a = bin(a)[2:].zfill(32); bin_b = bin(b)[2:].zfill(32)
	count_a = [0, 0]; count_b = [0, 0]

	for i in range(32):
		if bin_a[i] == '0':
			count_a[0] += 1
		else:
			count_a[1] += 1
		if bin_b[i] == '0':
			count_b[0] += 1
		else:
			count_b[1] += 1
	if count_a == count_b:
		return 'Yes'
	else:
		return 'No'

a = 8; b = 4

print(is_anagram_binary(8, 4))

'''
# Using Counter(iterable) method and dictionary comparison
# function to Check if binary representations
# of two numbers are anagram
from collections import Counter

def checkAnagram(num1, num2):

    bin1 = bin(num1)[2:] # convert numbers into in binary and remove first two characters
    bin2 = bin(num2)[2:] # of output string because bin function
    zeros = abs(len(bin1) - len(bin2)) # '0b' as prefix in output string

    if (len(bin1) > len(bin2)): # append zeros in shorter string
        bin2 = zeros * '0' + bin2
    else:
        bin1 = zeros * '0' + bin1


    dict1 = Counter(bin1); dict2 = Counter(bin2) # convert binary representations into dictionary

    if dict1 == dict2: # compare both dictionaries
        print('Yes')
    else:
        print('No')

if __name__ == '__main__': # driver program
    num1 = 8; num2 = 4
    checkAnagram(num1, num2)

# Using zfill

def is_anagram_binary(a, b):

	bin_a = bin(a)[2:].zfill(32); bin_b = bin(b)[2:].zfill(32)
	count_a = [0, 0]; count_b = [0, 0]

	for i in range(32):
		if bin_a[i] == '0':
			count_a[0] += 1
		else:
			count_a[1] += 1
		if bin_b[i] == '0':
			count_b[0] += 1
		else:
			count_b[1] += 1
	if count_a == count_b:
		return 'Yes'
	else:
		return 'No'

a = 8; b = 4

print(is_anagram_binary(8, 4)) # Output: True
'''
