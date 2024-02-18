from collections import Counter
items = \
    ['john', 'johnny', 'jackie', 'johnny', 'john', 'jackie', 'jamie', 'jamie', 'john', 'johnny', 'jamie',
     'johnny', 'john']

item_count = Counter(items)  # count the votes for persons and stores in the dictionary

max_items = max(item_count.values())  # find the maximum number of votes

# search for people having maximum votes and store in a list
list1 = [idx for idx in item_count.keys() if item_count[idx] == max_items]

res = sorted(list1)[0]  # sort the list and print the lexicographical smallest name

print(res)
