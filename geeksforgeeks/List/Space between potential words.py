import re
# Python3 code to add space between potential words using regex() + list comprehension
list1 = ['gfgBest', 'forGeeks', 'andComputerScience']

res = [re.sub(r'(\w)([A-Z])', r'\1 \2', item) for item in list1]

print('The space added list of strings:', res)
