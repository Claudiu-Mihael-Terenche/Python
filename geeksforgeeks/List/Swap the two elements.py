# Python3 program to swap elements at given positions using tuple variable

def swapPositions1(list, pos1, pos2):
    get = list[pos1], list[pos2] # storing the two elements as a pair in a tuple variable get
    list[pos2], list[pos1] = get # unpacking those elements
    return list


list1 = [23, 65, 19, 90]

pos1, pos2 = 1, 3

print(swapPositions1(list1, pos1 - 1, pos2 - 1))
