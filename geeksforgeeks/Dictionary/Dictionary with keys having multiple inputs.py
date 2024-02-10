import random as rn

dict1 = {}

x, y, z = 10, 20, 30
dict1[x, y, z] = x + y - z;

x, y, z = 5, 2, 4
dict1[x, y, z] = x + y - z;

print(dict1)

places = {("19.07'53.2", "72.54'51.0"):'Mumbai', ("28.33'34.1", "77.06'16.6"):'Delhi'}

lat = []
long = []
plc = []
for i in places:
	lat.append(i[0])
	long.append(i[1])
	plc.append(places[i[0], i[1]])

print('Lat:',lat, '\nLong:', long, '\nPlace:', plc)

data = {
	(1, 'John', 'Doe'): {'a': 'geeks', 'b': 'software', 'c': 75000},
	(2, 'Jane', 'Smith'): {'e': 30, 'f': 'for', 'g': 90000},
	(3, 'Bob', 'Johnson'): {'h': 35, 'i': 'project', 'j': 'geeks'},
	(4, 'Alice', 'Lee'): {'k': 40, 'l': 'marketing', 'm': 100000}
}

print(data[(1, 'John', 'Doe')]['a'])
print(data[(2, 'Jane', 'Smith')]['f'])
print(data[(3, 'Bob', 'Johnson')]['j'])

data[(1, 'John', 'Doe')]['a'] = {'b': 'marketing', 'c': 75000};
data[(3, 'Bob', 'Johnson')]['j'] = {'h': 35, 'i': 'project'};

print(data[(1, 'John', 'Doe')]['a']);
print(data[(3, 'Bob', 'Johnson')]['j']);

'''
# Python code to demonstrate a dictionary
# with multiple inputs in a key.
import random as rn

dict1 = {} # creating an empty dictionary

x, y, z = 10, 20, 30 # insert first triplet in dictionary
dict1[x, y, z] = x + y - z;

x, y, z = 5, 2, 4 # insert second triplet in dictionary
dict1[x, y, z] = x + y - z;

print(dict1)

# dictionary containing longitude and latitude of places
places = {("19.07'53.2", "72.54'51.0"):'Mumbai', ("28.33'34.1", "77.06'16.6"):'Delhi'}

# print(places)
# print('\n')

# Traversing dictionary with multi-keys and creating
# different lists from it

lat = []
long = []
plc = []
for i in places:
	lat.append(i[0])
	long.append(i[1])
	plc.append(places[i[0], i[1]])

print('Lat:',lat, '\nLong:', long, '\nPlace:', plc)

# Creating a dictionary with multiple inputs for keys
data = {
	(1, 'John', 'Doe'): {'a': 'geeks', 'b': 'software', 'c': 75000},
	(2, 'Jane', 'Smith'): {'e': 30, 'f': 'for', 'g': 90000},
	(3, 'Bob', 'Johnson'): {'h': 35, 'i': 'project', 'j': 'geeks'},
	(4, 'Alice', 'Lee'): {'k': 40, 'l': 'marketing', 'm': 100000}
}

# Accessing the values using the keys
print(data[(1, 'John', 'Doe')]['a'])
print(data[(2, 'Jane', 'Smith')]['f'])
print(data[(3, 'Bob', 'Johnson')]['j'])

data[(1, 'John', 'Doe')]['a'] = {'b': 'marketing', 'c': 75000};
data[(3, 'Bob', 'Johnson')]['j'] = {'h': 35, 'i': 'project'};

print(data[(1, 'John', 'Doe')]['a']);
print(data[(3, 'Bob', 'Johnson')]['j']);
'''
