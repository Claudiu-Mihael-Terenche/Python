# Using filter() method
str1 = 'geeksforgeeks'

y = filter(lambda x: str1.count(x) > 1, str1)

print(' '.join(set(y)))


# Version 3: using count() method

def find_dup_char(input02):
    x = []
    for i in input02:
        if i not in x and input02.count(i) > 1:
            x.append(i)
    print(' '.join(x))


if __name__ == '__main__':
    input2 = 'geeksforgeeks'
    find_dup_char(input2)

'''
def find_dup_char(input):
    x = filter(lambda x: input.count(x) > 1, input)
    print(' '.join(set(x)))


if __name__ == '__main__':
    input = 'geeksforgeeks'
    find_dup_char(input)
'''
