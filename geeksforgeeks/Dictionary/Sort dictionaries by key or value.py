# Creates a sorted dictionary (sorted by key)

dict1 = {'ravi': '10', 'rajnish': '9', 'sanjeev': '15', 'yash': '2', 'suraj': '32'}

dict2 = sorted(dict.items())

print(dict2)

def dictionairy():
    key_value = {}
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    # Note that it will sort in lexicographical order for mathematical way, change it to float
    print(sorted(key_value.items(), key=lambda kv:
    (kv[1], kv[0])))


def main():
    dictionairy()


if __name__ == '__main__':
    main()
