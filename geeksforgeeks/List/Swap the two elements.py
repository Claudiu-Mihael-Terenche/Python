# Python3 program to swap elements at given positions using tuple variable

def swap_positions(list0, pos01, pos02):
    get = list0[pos01], list0[pos02]  # storing the two elements as a pair in a tuple variable get
    list0[pos02], list0[pos01] = get  # unpacking those elements
    return list0


list1 = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swap_positions(list1, pos1 - 1, pos2 - 1))
