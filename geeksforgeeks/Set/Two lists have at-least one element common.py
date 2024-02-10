list1 = [1, 2, 3, 4, 5]; list2 = [5, 6, 7, 8, 9]

res1 = any(item in list2 for item in list1)

print(res1)

set1 = set(list1)
set2 = set(list2)

intersection = (set1 & set2)

res2 = len(intersection) != 0

print(res2)

if (set1 & set2):
    print('True')
else:
    print('False')

items = [item for item in list1 if item in list2]

res3 = len(items) != 0

print(res3)

'''
for item in list1:
    if item in list2:
        print('True')
    else:
        print('False')
'''
'''
# Using the any() function and the list comprehension method
def common_member(a, b):
	return any(i in b for i in a)

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_member(a, b)) # True

a =[1, 2, 3, 4, 5]
b =[6, 7, 8, 9]
print(common_member(a, b)) # False


# Python program to check
# if two lists have at-least
# one element common
# using set and property

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return True
    else:
        return False


a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_member(a, b))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_member(a, b))


# Python program to check
# if two lists have at-least
# one element common
# using traversal of list

def common_data(list1, list2):
    result = False

    # traverse in the 1st list
    for x in list1:

        # traverse in the 2nd list
        for y in list2:

            # if one common
            if x == y:
                result = True
                return result

    return result


# driver code
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_data(a, b))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_data(a, b))
'''
