def completePair(set1, set2):

    count = 0
    for str1 in set1:
        for str2 in set2:
            result = str1 + str2

            tmpSet = set([ch for ch in result if (ord(ch) >= ord('a') and ord(ch) <= ord('z'))])
            if len(tmpSet) == 26:
                count = count + 1
    print(count)


if __name__ == '__main__':
    set1 = ['abcdefgh', 'geeksforgeeks', 'lmnopqrst', 'abc']
    set2 = ['ijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'defghijklmnopqrstuvwxyz']
    completePair(set1, set2)

'''
# Using Set data structure
# function to find pairs of complete strings in two sets of strings

def completePair(set1, set2):
    # consider all pairs of string from set1 and set2
    count = 0
    for str1 in set1:
        for str2 in set2:
            result = str1 + str2

            # push all alphabets of concatenated string into temporary set
            tmpSet = set([ch for ch in result if (ord(ch) >= ord('a') and ord(ch) <= ord('z'))])
            if len(tmpSet) == 26:
                count = count + 1
    print(count)


if __name__ == '__main__':
    set1 = ['abcdefgh', 'geeksforgeeks', 'lmnopqrst', 'abc']
    set2 = ['ijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', 'defghijklmnopqrstuvwxyz']
    completePair(set1, set2)
'''
