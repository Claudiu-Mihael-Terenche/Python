from itertools import permutations


# Function to find permutations of a given string

def all_permutations(str01):
    perm_list = permutations(str01)  # get all permutations of string 'ABC'

    for item in list(perm_list):
        print(''.join(item))  # print all permutations


if __name__ == '__main__':
    str1 = 'ABC'
    all_permutations(str1)
