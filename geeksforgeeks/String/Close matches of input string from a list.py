# Function to find all close matches of input string in given list of possible strings

from difflib import get_close_matches

def closeMatches(patterns, word): print(get_close_matches(word, patterns))


if __name__ == '__main__':
	word = 'appel'
	patterns = ['ape', 'apple', 'peach', 'puppy']
	closeMatches(patterns, word)
