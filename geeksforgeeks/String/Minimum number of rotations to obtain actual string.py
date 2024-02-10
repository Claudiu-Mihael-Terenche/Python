def findRotations(str1, str2):

    x = 0 # to count left rotations of string
    y = 0 # to count right rotations of string

    m = str1

    while True:

        m = m[len(m) - 1] + m[:len(m) - 1] # left rotating the string

        if (m == str2): # checking if rotated and actual string are equal
            x += 1
            break
        else:
            x += 1
            if x > len(str2):
                break

    while True:

        str1 = str1[1:len(str1)] + str1[0] # right rotating the string

        if (str1 == str2): # checking if rotated and actual string are equal
            y += 1
            break
        else:
            y += 1
            if y > len(str2):
                break

    if x < len(str2):
        print(min(x, y)) # printing the minimum number of rotations
    else:
        print('Given strings are not of same kind')


findRotations('sgeek', 'geeks')
