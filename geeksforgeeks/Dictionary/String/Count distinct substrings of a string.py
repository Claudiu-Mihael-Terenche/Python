def main():
    str1 = 'abcd'

    substrings = set()  # set to store distinct substrings

    for i in range(len(str1)):  # iterate over all possible substrings and add them to the set
        for j in range(i, len(str1)):
            substrings.add(str1[i:j + 1])
    print(len(substrings))  # output the number of distinct substrings


if __name__ == '__main__':
    main()
