# Python3 program to find a list of uncommon words using the set() and difference() method

# function to return all uncommon words
def UncommonWords(str1, str2):
    # split the strings str1 and str2 into words and create sets
    A = set(str1.split())
    B = set(str2.split())

    # find the uncommon words in A and B and combine them
    uncommonWords = A.difference(B).union(B.difference(A))

    # convert the set to a list and return
    return list(uncommonWords)


str1 = 'Geeks for Geeks'; str2 = 'Learning from Geeks for Geeks'

print(*UncommonWords(str1, str2))
