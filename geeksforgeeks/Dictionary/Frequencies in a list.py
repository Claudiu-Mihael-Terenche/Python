def count_frequency(list0):
    count = {}  # Creating an empty dictionary
    for i in list0:
        count[i] = count.get(i, 0) + 1
    return count


if __name__ == '__main__':
    list1 = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
    print(count_frequency(list1))
