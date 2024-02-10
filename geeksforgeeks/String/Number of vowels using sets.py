import re

str1 = 'GeeksforGeeks'

vowels = 'aeiouAEIOU'

res1 = len([item for item in str1 if item in vowels])

print('No. of vowels:', res1)

res2 = sum(str1.count(item) for item in vowels)

print(res2)

str3 = 'GeeksforGeeks'

vowels3 = r'[aeiouAEIOU]'

count3 = len(re.findall(vowels3, str3))

print(count3)

def vowel_count4(str4):

    count4 = 0

    vowel4 = set('aeiouAEIOU')

    for alphabet in str4:
        if alphabet in vowel4:
            count4 += count4
    print('No. of vowels:', count4)


str4 = 'GeeksforGeeks'

vowel_count4(str4)

'''
# Using list comprehension

str1 = 'GeeksforGeeks'

vowels = 'aeiouAEIOU'

res1 = len([item for item in str1 if item in vowels])

print('No. of vowels:', res1)

def vowel_count1(str1):

    vowels = 'aeiouAEIOU'

    # using list comprehension to count the number of vowels in the string
    count1 = len([item for item in str1 if item in vowels])

    print('No. of vowels:', count1)


str1 = 'GeeksforGeeks'

vowels = 'aeiouAEIOU'

vowel_count1(str1)

# Version 2: using count() method

# str2 = 'GeekforGeeks!'
# vowels2 = 'aeiouAEIOU'

res2 = sum(str1.count(item) for item in vowels)

print(res2)

# Version 3: using regex

import re

str3 = 'GeeksforGeeks'

vowels3 = r'[aeiouAEIOU]'

count3 = len(re.findall(vowels3, str3))

print(count3)

# Version 4: Python3 code to count vowel in a string using set()

# function to count vowel

def vowel_count4(str4):
    count4 = 0

    # creating a set of vowels
    vowel4 = set('aeiouAEIOU')

    for alphabet in str4:
        if alphabet in vowel4:
            count4 += count4
    print('No. of vowels:', count4)


str4 = 'GeeksforGeeks'

vowel_count4(str4)
'''
