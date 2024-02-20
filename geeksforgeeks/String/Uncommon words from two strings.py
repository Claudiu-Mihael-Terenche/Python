# Python3 program to find a list of uncommon words using the set() and difference() method
# to return all uncommon words
str1 = 'Geeks for Geeks'
str2 = 'Learning from Geeks for Geeks'

# split the strings str1 and str2 into words and create sets
a = set(str1.split())
b = set(str2.split())

# find the uncommon words in a and b and combine them
uw = a.difference(b).union(b.difference(a))

# convert the set to a list and return
res = list(uw)

print(*res)
