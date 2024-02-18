from collections import Counter
# Function to find the size of the largest subset of anagram words using Counter() method


def max_anagram_size(input0):
    input0 = input0.split(' ')  # split input string separated by space

    # sort each string in given a list of strings
    for i in range(len(input0)):
        input0[i] = ''.join(sorted(input0[i]))

    # now create a dictionary using counter-method which will have strings as a key and their frequencies as value
    freq_dict = Counter(input0)

    print(max(freq_dict.values()))  # get maximum value of frequency


if __name__ == '__main__':
    input1 = 'ant magenta magnate tan gnamate'
    max_anagram_size(input1)

# Using lambda

words1 = ['ant', 'magenta', 'magnate', 'tan', 'gnamate']

max_anagrams = max(list(map(lambda x: sum(map(lambda y: Counter(y) == Counter(x), words1)), words1)), default=0)

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


words3 = ['ant', 'magenta', 'magnate', 'tan', 'gnamate']

print(largest_anagram_subset_size(words3))
