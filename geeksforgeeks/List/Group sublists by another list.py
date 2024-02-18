# Python3 code to group sublist by another list using loop + generator(yield)

def grp_item(list01, list02):  # helper function
    temp = []
    for item in list01:
        if item in list02:
            if temp:
                yield temp
                temp = []
            yield item
        else:
            temp.append(item)
    if temp:
        yield temp


list1 = [8, 5, 9, 11, 3, 7]
list2 = [9, 11]

# Group sublist by another list using loop + generator(yield)

res = list(grp_item(list1, list2))

print('The grouped list is:', res)
