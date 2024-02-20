"""
gfg = 'geeksforgeeks'
print(gfg[::-1]) # reverse string
print(''.join(reversed(gfg))) # reverse string
print(gfg[0])
print(gfg[5:8]) # slice string

# update char of a str
list1 = list(gfg)
list1[5:8] = 'to'
gfg2 = ''.join(list1)
print(gfg2)

# Version 2: update char of a string
gfg3 = gfg[0:5] + 'to' + gfg[8:]
print(gfg3)

# format a str
str1 = "{1} {0} {2}".format('geeks', 'for', 'life')
print(str1)

# formatting of integers
str2 = '{0:b}'.format(16)
print('\nBinary representation of 16 is ')
print(str2)

# formatting of floats
str3 = '{0:e}'.format(165.6458)
print('\nExponent representation of 165.6458 is ')
print(str3)

# rounding off integers
str4 = '{0:.2f}'.format(1/6)
print('\none-sixth is: ')
print(str4)

# iteration by for loop on string
str1 = 'Hello world'
for item in str1:
print(item)

input(str.split()) # multiple input

python String constants
Built-In Function

description

string.ascii_letters
Concatenation of the ascii_lowercase and ascii_uppercase constants.

string.ascii_lowercase
Concatenation of lowercase letters

string.ascii_uppercase
Concatenation of uppercase letters

string.digits
Digit in strings

string.hexdigits
Hexadigit in strings

string.letters

concatenation of the strings lowercase and uppercase

string.lowercase

a string must contain lowercase letters.

string.octdigits

octadigit in a string

string.punctuation

ASCII characters having punctuation characters.

string.printable

string of characters which are printable

string.endswith()
Returns True if a string ends with the given suffix otherwise returns False

string.startswith()
Returns True if a string starts with the given prefix otherwise returns False

string.isdigit()
Returns “True” if all characters in the string are digits, Otherwise, It returns “False”.

string.isalpha()
Returns “True” if all characters in the string are alphabets, Otherwise, It returns “False”.

string.isdecimal()
Returns true if all characters in a string are decimal.

str.format()
one of the string formatting methods in Python3, which allows multiple substitutions and value formatting.

string.index
Returns the position of the first occurrence of substring in a string

string.uppercase

a string must contain uppercase letters.

string.whitespace
A string containing all characters that are considered whitespace.

string.swapcase()
Method converts all uppercase characters to lowercase and vice versa of the given string, and returns it

replace()
returns a copy of the string where all occurrences of a substring are replaced with another substring.

deprecated string functions
Built-In Function

description

string.Isdecimal
Returns true if all characters in a string are decimal

string.Isalnum
Returns true if all the characters in a given string are alphanumeric.

string.Istitle
Returns True if the string is a title cased string

string.partition
splits the string at the first occurrence of the separator and returns a tuple.

string.Isidentifier
Check whether a string is a valid identifier or not.

string.len
Returns the length of the string.

string.rindex
Returns the highest index of the substring inside the string if substring is found.

string.Max
Returns the highest alphabetical character in a string.

string.min
Returns the minimum alphabetical character in a string.

string.splitlines
Returns a list of lines in the string.

string.capitalize
Returns a word with its first character capitalized.

string.expandtabs
Expand tabs in a string replacing them with one or more spaces

string.find
Return the lowest indexing a sub string.

string.rfind
finds the highest index.

string.count
Returns the number of (non-overlapping) occurrences of substring sub in string

string.lower
Returns a copy of s, but with an upper case, letters converted to a lower case.

string.split
Returns a list of the words of the string, If the optional second argument sep is absent or None

string.rsplit()
Returns a list of the words of the string s, scanning s from the end.

repartition()
Method splits the given string into three parts

string.splitfields

return a list of the words of the string when only used with two arguments.

string.join
Concatenate a list or tuple of words with intervening occurrences of sep.

string.strip()
It returns a copy of the string with both leading and trailing white spaces removed

string.lstrip
Returns a copy of the string with leading white spaces removed.

string.rstrip
Returns a copy of the string with trailing white spaces removed.

string.swapcase
Converts lower case letters to an upper case and vice versa.

string.translate
Translate the characters using table

string.upper
lower case letters converted to an upper case.

string.ljust
left-justify in a field of given width.

string.rjust
Right-justify in a field of given width.

string.center()
Center-justify in a field of given width.

string-zfill
Pad a numeric string on the left with zero digits until the given width is reached.

string.replace
Returns a copy of string s with all occurrences of substring old replaced by new.

string.casefold()
Returns the string in lowercase which can be used for caseless comparisons.

string.encode
Encodes the string into any encoding supported by Python; the default encoding is utf-8.

string.maketrans
Returns a translation table usable for str.translate()
"""
