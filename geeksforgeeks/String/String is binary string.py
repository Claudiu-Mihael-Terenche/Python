import re


def check1(str01):
    if all((letter in '01') for letter in str01):
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    str1 = '101011000111'
    str2 = '201000001'

    print(check1(str1))
    print(check1(str2))


def check2(str02):
    t = '01'

    count = 0
    for item02 in str02:
        if item02 not in t:
            count = 1
            break
        else:
            pass

    if count:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    str1 = '001021010001010'
    check2(str1)

str2 = '1001010'
c = re.compile('[^01]')

if len(c.findall(str2)):
    print('No')
else:
    print('Yes')


def check3(str03):
    try:
        int(str03, 2)
    except ValueError:
        return 'No'
    return 'Yes'


if __name__ == '__main__':
    str1 = "101011000111"
    str2 = "201000001"

    print(check3(str1))
    print(check3(str2))

str1 = '01010101010'

if str1.count('0') + str1.count('1') == len(str1):
    print('Yes')
else:
    print('No')

binary = '01'

for item in binary:
    str1 = str1.replace(item, '')
if len(str1) == 0:
    print('Yes')
else:
    print('No')


def is_binary_string4(str04):
    unique_items = {item04 for item04 in str04}

    return unique_items.issubset({'0', '1'})


if __name__ == '__main__':
    str1 = '101011000111'
    str2 = '201000001'

    print(is_binary_string4(str1))
    print(is_binary_string4(str2))


def is_binary_string5(str05):
    regex = r'[^01]'

    if re.search(regex, str05):
        return False
    else:
        return True


print(is_binary_string5('01010101010'))
print(is_binary_string5('geeks101'))

'''
# Version 5: Python program to check if a string is binary or not using all()

# function for checking the string is accepted or not


def check5(str5):
    if all((letter in '01') for letter in str5):
        return 'Yes'
    return 'No'


# driver code
if __name__ == '__main__':

    str51 = '101011000111'
    str52 = '201000001'

    # function calling
    print(check5(str51))
    print(check5(str52))

# Version 1: Python program to check if a string is binary or not using simple iteration

# function for checking the string is accepted or not


def check1(str1):

    # initialize the variable t with '01' string
    t = '01'

    # initialize the variable count with 0 value
    count = 0

    # looping through each character of the string .
    for item1 in str1:

        # check the character is present in string t or not.
        # if this condition is true assign 1 to the count variable and break out of the for loop otherwise pass
        if item1 not in t:
            count = 1
            break
        else:
            pass

    # after coming out of the loop check value of count is non-zero or not
    # if the value is non-zero the en condition is true and string is not accepted otherwise string is accepted
    if count:
        print('No')
    else:
        print('Yes')


# driver code
if __name__ == '__main__':

    str1 = '001021010001010'

    # function calling
    check1(str1)

# Version 8: using regular expressions
# import library
import re

sampleInput = '1001010'

# regular expression to find the strings which have characters other than 0 and 1
c = re.compile('[^01]')

# use findall() to get the list of strings that have characters other than 0 and 1.
if(len(c.findall(sampleInput))):
    print('No') # if length of list > 0 then it is not binary
else:
    print('Yes') # if length of list = 0 then it is binary

# Version 2: Python program to check if a string is binary or not

# function for checking the string is accepted or not


def check2(str2):
    try:
        # this will raise value error if string is not of base 2
        int(str2, 2)
    except ValueError:
        return 'No'
    return 'Yes'


# driver code
if __name__ == '__main__':

    string21 = "101011000111"
    string22 = "201000001"

    # function calling
    print(check2(str21))
    print(check2(str22))

# Version 3: using count() function
str3 = '01010101010'
if(str3.count('0') + str3.count('1') == len(str3)):
    print('Yes')
else:
    print('No')

# Version 4: Python program to check string is binary or not using replace() and len() methods
str4 = '01010121010'
binary = '01'
for item4 in binary:
    str4 = str4.replace(item4,'')
if(len(str4) == 0):
    print('Yes')
else:
    print('No')

# Version 6: using issubset() method
def is_binary_string6(str6):
    # use set comprehension to extract all unique characters from the string
    unique_items = {item6 for item6 in str6}
    # check if the unique characters are only 0 and 1
    return unique_items.issubset({'0', '1'})

# driver code
if __name__ == '__main__':

    str61 = '101011000111'
    str62 = '201000001'

    # function calling
    print(is_binary_string6(str61))
    print(is_binary_string6(str62))

# Version 7: using re.search()
import re


def is_binary_string7(str7):
    # define regular expression
    regex = r'[^01]'

    # search for regular expression in string
    if re.search(regex, str7):
        return False
    else:
        return True


# examples
print(is_binary_string7('01010101010'))  # Output: Yes
print(is_binary_string7('geeks101'))  # Output: No
'''
