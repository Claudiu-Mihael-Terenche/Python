# Python3 code to extract words starting with K in string list using list comprehension + split()
list1 = ['Gfg is best', 'Gfg is for geeks', 'I love G4G']
K = 'g'

res = [item for temp in list1 for item in temp.split() if item[0].lower() == K.lower()]

print('The filtered elements:', res)
