from itertools import permutations

# Function to find permutations of a given string

def allPermutations(str):

    permList = permutations(str) # get all permutations of string 'ABC'

    for item in list(permList): print(''.join(item)) # print all permutations


if __name__ == '__main__':
    str = 'ABC'
    allPermutations(str)
