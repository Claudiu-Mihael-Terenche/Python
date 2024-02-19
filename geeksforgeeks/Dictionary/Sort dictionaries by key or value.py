# Creates a sorted dictionary (sorted by key)
dict1 = {'ravi': '10', 'rajnish': '9', 'sanjeev': '15', 'yash': '2', 'suraj': '32'}

dict2 = sorted(dict1.items())

print(dict2)


def dictionary():
    key_value = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}

    # Note that it will sort in lexicographical order for mathematical way, change it to float
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))


def main():
    dictionary()


if __name__ == '__main__':
    main()
