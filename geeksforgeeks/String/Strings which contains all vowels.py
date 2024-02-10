import collections

def check1(str1):

	vowels = 'aeiou'

	if all(val in str1.lower() for val in vowels):
		return 'Accepted'
	return 'Not accepted'


str1 = 'SEEquoiaL'

print(check1(str1))

def check2(str1):

    if set('aeiou').issubset(set(str1.lower())):
        return 'Accepted'
    return 'Not accepted'


if __name__ == '__main__':
    str1 = 'SEEquoiaL'
    print(check2(str1))

def check3(str1):
	if len(set(str1.lower()).intersection('aeiou')) >= 5:
		return ('accepted')
	else:
		return ('not accepted')


if __name__ == '__main__':
	str1 = 'SEEquoiaL'
	print(check3(str1))

def check4(str1):

    str1 = str1.lower()

    vowels = set('aeiou')

    s = set({})

    for item in str1:
        if item in vowels:
            s.add(item)
        else:
            pass

    if len(s) == len(vowels):
        print('Accepted')
    else:
        print('Not accepted')


if __name__ == '__main__':
    str1 = 'SEEquoiaL'
    check4(str1)

def check5(str1):

    counter = collections.Counter(str1.lower())

    vowels = set('aeiou')

    vowel_count = 0

    for vowel in vowels:
        if counter[vowel] > 0:
            vowel_count += 1

    if vowel_count == len(vowels):
        print('Accepted')
    else:
        print('Not accepted')

str1 = 'SEEquoiaL'
check5(str1)

'''
# Python program to accept the strings which contains all the vowels

# function for check if string is accepted or not using all() method

def check(str1):
	vowels1 = 'aeiou' # storing vowels
	if all(vowel1 in str1.lower() for vowel1 in vowels1):
		return 'Accepted'
	return 'Not accepted'


# initializing string
str1 = 'SEEquoiaL'
# test the function
print(check(str1))

# Version 2: Python program to accept the strings which contains all the vowels

# function for check if string is accepted or not
def check(str2):
    # checking if 'aeiou' is a subset of the set of all letters in the string
    if set('aeiou').issubset(set(str2.lower())):
        return 'Accepted'
    return 'Not accepted'


# driver code
if __name__ == '__main__':
    str2 = 'SEEquoiaL'

    # calling function
    print(check(str2))

# Version 3
def check(str3):
	if len(set(str3.lower()).intersection('aeiou')) >= 5:
		return ('accepted')
	else:
		return ('not accepted')


# driver code
if __name__ == '__main__':
	str3 = 'geeksforgeeks'
	print(check(str3))

# Version 4: Python program to accept the strings which contains all the vowels

# function for check if string is accepted or not
def check(str4):
    str4 = str4.lower()

    # set() function convert "aeiou" string into set of characters
    # i.e.vowels = {'a', 'e', 'i', 'o', 'u'}
    vowels4 = set('aeiou')

    # set() function convert empty dictionary into empty set
    s = set({})

    # looping through each character of the string
    for item4 in str4:

        # Check for the character is present inside the vowels set or not.
        # If present, then add into the set s by using add method
        if item4 in vowels4:
            s.add(item4)
        else:
            pass

    # check the length of set s equal to length of vowels set or not. If equal, string is accepted otherwise not
    if len(s) == len(vowels4):
        print('Accepted')
    else:
        print('Not accepted')


# driver code
if __name__ == '__main__':
    str4 = 'SEEquoiaL'

    # calling function
    check(str4)

# Version 5
import collections


def check(str5):
    # create a Counter object to count the occurrences of each character
    counter = collections.Counter(str5.lower())

    # set of vowels
    vowels5 = set('aeiou')

    # counter for the number of vowels present
    vowel_count = 0

    # check if each vowel is present in the string
    for vowel5 in vowels5:
        if counter[vowel5] > 0:
            vowel_count += 1

    # check if all vowels are present
    if vowel_count == len(vowels5):
        print('Accepted')
    else:
        print('Not accepted')


# test the function
str5 = 'SEEquoiaL'
check(str5)
'''
