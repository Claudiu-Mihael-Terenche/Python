from collections import OrderedDict


def kth_repeating(input0, k):
    dict0 = OrderedDict.fromkeys(input0, 0)

    for ch in input0:
        dict0[ch] += 1

    non_repeat_dict = [key for (key, value) in dict0.items() if value == 1]

    if len(non_repeat_dict) < k:
        return 'Less than k non-repeating characters in input'
    else:
        return non_repeat_dict[k - 1]


if __name__ == '__main__':
    input1 = 'geeksforgeeks'
    k1 = 3
    print(kth_repeating(input1, k1))

'''
# Using list comprehension and OrderedDict
# Function to find kth non repeating character
# in string
from collections import OrderedDict

def kthRepeating(input, k):
    # OrderedDict returns a dictionary data structure having characters of input
    # string as keys in the same order they were inserted and 0 as their default value
    dict = OrderedDict.fromkeys(input, 0)

    for ch in input: dict[ch] += 1 # now traverse input string to calculate frequency of each character

    # now extract list of all keys whose values 1 from dict Ordered Dictionary
    nonRepeatDict = [key for (key, value) in dict.items() if value == 1]

    if len(nonRepeatDict) < k: # now return (k-1)th character from above list
        return 'Less than k non-repeating characters in input'
    else:
        return nonRepeatDict[k - 1]


if __name__ == '__main__':
    input = 'geeksforgeeks'
    k = 3
    print(kthRepeating(input, k))
'''
