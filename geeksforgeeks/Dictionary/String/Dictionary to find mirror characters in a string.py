def mirrorChars(input, k):

    original = 'abcdefghijklmnopqrstuvwxyz' # create dictionary

    reverse = original[::-1] # 'zyxwvutsrqponmlkjihgfedcba'

    dictChars = dict(zip(original, reverse))

    prefix = input[0:k - 1] # separate out string after length k to change characters in mirror
    suffix = input[k - 1:]

    mirror = ''

    for i in range(0, len(suffix)): # change into mirror
        mirror = mirror + dictChars[suffix[i]]
    print(prefix + mirror) # concat prefix and mirrored part



if __name__ == '__main__':
    input = 'paradox'
    k = 3
    mirrorChars(input, k)
