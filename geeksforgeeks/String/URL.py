# Python code to find the URL from an input string using startswith() method

def find1(str01):
    word = str01.split()
    res1 = []
    for item in word:
        if item.startswith("https:") or item.startswith("http:"):
            res1.append(item)
    return res1


str1 = ('My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of '
        'https://www.geeksforgeeks.org/')

print('Urls:', find1(str1))


# Approach 2: Python code to find the URL from an input string using find() method

def find2(str02):
    word = str02.split()
    res2 = []
    for item in word:
        if item.find("https:") == 0 or item.find("http:") == 0:
            res2.append(item)
    return res2


str1 = ('My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of '
        'https://www.geeksforgeeks.org/')

print('Urls:', find2(str1))
