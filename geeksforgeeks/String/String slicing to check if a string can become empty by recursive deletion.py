def check_empty(str01, pattern):

    if len(str01) == 0 and len(pattern) == 0:
        return 'true'

    if len(pattern) == 0:
        return 'false'

    while len(str01) != 0:

        index = str01.find(pattern)

        if index == (-1):
            return 'false'

        str01 = str01[0:index] + str01[index + len(pattern):]
    return 'true'


if __name__ == '__main__':
    str1 = 'GEEGEEKSKS'
    pattern1 = 'GEEKS'
    print(check_empty(str1, pattern1))

'''
# Using find() method of string to search given pattern sub-string
def checkEmpty(str1, pattern):
    # if both are empty
    if len(str1) == 0 and len(pattern) == 0:
        return 'true'

    # if only pattern is empty
    if len(pattern) == 0:
        return 'false'

    while (len(str1) != 0):

        # find sub-string in main string
        index = str1.find(pattern)

        # check if sub-string founded or not
        if (index == (-1)):
            return 'false'

        # slice input string in two parts and concatenate
        str1 = str1[0:index] + str1[index + len(pattern):]
    return 'true'


if __name__ == '__main__':
    str1 = 'GEEGEEKSKS'
    pattern = 'GEEKS'
    print(checkEmpty(str1, pattern))
'''
