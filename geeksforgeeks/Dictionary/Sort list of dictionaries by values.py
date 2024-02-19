from operator import itemgetter
list1 = [{'name': 'Nandini', 'age': 20}, {'name': 'Manjeet', 'age': 20}, {'name': 'Nikhil', 'age': 19}]

print('The list printed sorting by age:', sorted(list1, key=itemgetter('age')))
print('The list printed sorting by age and name:', sorted(list1, key=itemgetter('age', 'name')))
print('The list printed sorting by age in descending order:', sorted(list1, key=itemgetter('age'), reverse=True))

print('The list printed sorting by age:', sorted(list1, key=lambda i: i['age']))
print('The list printed sorting by age and name:', sorted(list1, key=lambda i: (i['age'], i['name'])))
print('The list printed sorting by age in descending order:', sorted(list1, key=lambda i: i['age'], reverse=True))

'''
# Python code demonstrate the working of sorted() and itemgetter

# importing "operator" for implementing itemgetter
from operator import itemgetter

list = [{'name': 'Nandini', 'age': 20}, {'name': 'Manjeet', 'age': 20}, {'name': 'Nikhil', 'age': 19}]

# using sorted and itemgetter to print list sorted by age
print('The list printed sorting by age:', sorted(list, key=itemgetter('age')))
print('The list printed sorting by age and name:', sorted(list, key=itemgetter('age', 'name')))
print('The list printed sorting by age in descending order:', sorted(list, key=itemgetter('age'), reverse=True))

# using sorted and itemgetter to print
# list sorted by both age and name
# notice that "Manjeet" now comes before "Nandini"

# print('The list printed sorting by age and name:', sorted(list, key=itemgetter('age', 'name')))

# using sorted and itemgetter to print list
# sorted by age in descending order

# print('The list printed sorting by age in descending order:', sorted(list, key=itemgetter('age'), reverse=True))

# Python code demonstrate the working of
# sorted() with lambda

# Initializing list of dictionaries

# list = [{"name": "Nandini", "age": 20}, {"name": "Manjeet", "age": 20}, {"name": "Nikhil", "age": 19}]

# using sorted and lambda to print list sorted
# by age

print('The list printed sorting by age:', sorted(list, key=lambda i: i['age']))
print('The list printed sorting by age and name:', sorted(list, key=lambda i: (i['age'], i['name'])))
print('The list printed sorting by age in descending order:', sorted(list, key=lambda i: i['age'], reverse=True))

# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# now comes before "Nandini"

# print('The list printed sorting by age and name:', sorted(list, key=lambda i: (i['age'], i['name'])))

# using sorted and lambda to print list sorted
# by age in descending order

# print('The list printed sorting by age in descending order:', sorted(list, key=lambda i: i['age'], reverse=True))
'''
