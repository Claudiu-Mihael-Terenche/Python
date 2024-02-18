def mirror_chars(input0, k):
    original = 'abcdefghijklmnopqrstuvwxyz'  # create dictionary

    reverse = original[::-1]  # 'zyxwvutsrqponmlkjihgfedcba'

    dict_chars = dict(zip(original, reverse))

    prefix = input0[0:k - 1]  # separate out string after length k to change characters in mirror
    suffix = input0[k - 1:]

    mirror = ''

    for i in range(len(suffix)):  # change into mirror
        mirror = mirror + dict_chars[suffix[i]]
    print(prefix + mirror)  # concat prefix and mirrored part


if __name__ == '__main__':
    input1 = 'paradox'
    k1 = 3
    mirror_chars(input1, k1)
