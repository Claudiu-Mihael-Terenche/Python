def all_anagram(input0):
    dict0 = {}

    for strVal in input0:
        key = ''.join(sorted(strVal))
        if key in dict0.keys():
            dict0[key].append(strVal)
        else:
            dict0[key] = []
            dict0[key].append(strVal)
    output = ''

    for key, value in dict0.items():
        output = output + ' '.join(value) + ' '
    return output


if __name__ == '__main__':
    input1 = ['cat', 'dog', 'tac', 'god', 'act']
    print(all_anagram(input1))

'''
# Function to return all anagrams together
def allAnagram(input):

    dict = {} # empty dictionary which holds subsets of all anagrams together

    for strVal in input: # traverse list of strings
        key = ''.join(sorted(strVal)) # sorted(iterable) method accepts any iterable and returns list of items
        if key in dict.keys(): # in ascending order
            dict[key].append(strVal) # now check if key exist in dictionary or not.
        else: # If yes then simply append the strVal into the list of it's corresponding key.
            dict[key] = [] # If not then map empty list onto key and then start appending values
            dict[key].append(strVal)
    output = '' # traverse dictionary and concatenate values of keys together

    for key, value in dict.items():
        output = output + ' '.join(value) + ' '
    return output

if __name__ == '__main__': # driver function
    input = ['cat', 'dog', 'tac', 'god', 'act']
    print(allAnagram(input))
'''
