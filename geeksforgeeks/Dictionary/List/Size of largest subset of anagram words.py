from collections import Counter

# Function to find the size of largest subset of anagram words using Counter() method

def maxAnagramSize(input):

	input = input.split(' ') # split input string separated by space

	# sort each string in given list of strings
	for i in range(0, len(input)): input[i] = ''.join(sorted(input[i]))


	# now create dictionary using counter method which will have strings as key and their frequencies as value
	freqDict = Counter(input)

	print(max(freqDict.values())) # get maximum value of frequency

if __name__ == '__main__':
	input = 'ant magenta magnate tan gnamate'
	maxAnagramSize(input)

# Using lambda

words = ['ant', 'magenta', 'magnate', 'tan', 'gnamate']

max_anagrams = max(list(map(lambda x: sum(map(lambda y: Counter(y) == Counter(x), words)), words)), default=0)

print(max_anagrams)

# Using dictionary

def largest_anagram_subset_size(words):
	anagram_dict = {}
	for word in words:
		sorted_word = ''.join(sorted(word))
		if sorted_word not in anagram_dict:
			anagram_dict[sorted_word] = []
		anagram_dict[sorted_word].append(word)
	max_count = max([len(val) for val in anagram_dict.values()])
	return max_count

words = ['ant', 'magenta', 'magnate', 'tan', 'gnamate']

print(largest_anagram_subset_size(words))
