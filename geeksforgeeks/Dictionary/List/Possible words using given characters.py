def possible_words(dict, chars):

	chars_set = set(chars)

	res1 = []
	for word in dict:
		if set(word).issubset(chars_set):
			res1.append(word)
	return res1


dict = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
chars = ['e', 'o', 'b', 'a', 'm', 'g', 'l']

print(*possible_words(dict, chars))

def find_words(dict, chars, word=''):

    if word in dict: print(word)

    for char in chars:
        new_chars = chars.copy()
        new_chars.remove(char)
        find_words(dict, new_chars, word + char)


find_words(dict, chars)

'''
# Version 1
def possible_words(dict, chars):

	chars_set = set(chars)

	res1 = []
	for word in dict:
		if set(word).issubset(chars_set):
			res1.append(word)
	return res1


dict = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
chars = ['e', 'o', 'b', 'a', 'm', 'g', 'l']

print(*possible_words(dict, chars))

# Version 2
def find_words(dict, chars, word=''):

    if word in dict: print(word) # base case: if the word is in the dictionary, print it

    # recursive case: for each character in the characters list, make a new list of characters
    # with that character removed, and call find_words with the new list of characters and the
    # current word appended with the current character
    for char in chars:
        new_chars = chars.copy()
        new_chars.remove(char)
        find_words(dict, new_chars, word + char)


# example usage
# dict2 = ["go", "bat", "me", "eat", "goal", "boy", "run"]
# chars2 = ['e', 'o', 'b', 'a', 'm', 'g', 'l']

find_words(dict, chars)
'''
