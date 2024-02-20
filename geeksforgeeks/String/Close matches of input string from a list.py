# Function to find all close matches of input string in given list of possible strings
from difflib import get_close_matches


def close_matches(patterns, word): print(get_close_matches(word, patterns))


if __name__ == '__main__':
    word1 = 'appel'
    patterns1 = ['ape', 'apple', 'peach', 'puppy']
    close_matches(patterns1, word1)
