def extract_path(dict1, path_way):
	if not dict1:
		return [path_way]
	temp = []
	for key in dict1:
		temp.extend(extract_path(dict1[key], path_way + [key]))
	return temp

def hlper_fnc(dict1):
	all_paths = extract_path(dict1, [])
	res = {}
	for path in all_paths:
		front = res
		for ele in path[::-1]:
			if ele not in front:
				front[ele] = {}
			front = front[ele]
	return res


dict1 = {'a': {'b': {'c': {}}}, 'd': {'e': {}}, 'f': {'g': {'h': {}}}}

res = hlper_fnc(dict1)

print('The inverted dictionary:', res)

'''
# Python3 code to demonstrate working of
# Inversion in nested dictionary
# Using loop + recursion

# utility function to get all paths till end

def extract_path(dict1, path_way):
	if not dict1:
		return [path_way]
	temp = []
	for key in dict1:
		temp.extend(extract_path(dict1[key], path_way + [key]))
	return temp

# function to compute inversion
def hlper_fnc(dict1):
	all_paths = extract_path(dict1, [])
	res = {}
	for path in all_paths:
		front = res
		for ele in path[::-1]:
			if ele not in front:
				front[ele] = {}
			front = front[ele]
	return res


dict1 = {'a': {'b': {'c': {}}}, 'd': {'e': {}}, 'f': {'g': {'h': {}}}}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# calling helper function for task

res = hlper_fnc(dict1)

print('The inverted dictionary:', res)
'''
