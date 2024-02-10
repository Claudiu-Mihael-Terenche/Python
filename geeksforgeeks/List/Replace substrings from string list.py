# Python3 code to replace substrings from string list using replace() + list comprehension

list1 = ['GeeksforGeeks', 'is', 'Best', 'For', 'Geeks', 'And', 'Computer Science']
list2 = [['Geeks', 'Gks'], ['And', '&'], ['Computer', 'Comp']]

res1 = [sub.replace(sub2[0], sub2[1]) for sub in list1 for sub2 in list2 if sub2[0] in sub]

print ('The list after replacement:', res1)
