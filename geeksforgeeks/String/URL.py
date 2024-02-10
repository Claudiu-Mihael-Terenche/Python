# Python code to find the URL from an input string using startswith() method

def Find1(str1):
    word1 = str1.split()
    res1 = []
    for item1 in word1:
        if item1.startswith("https:") or item1.startswith("http:"):
            res1.append(item1)
    return res1


str1 = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'

print('Urls:', Find1(str1))

# Approach 2: Python code to find the URL from an input string using find() method

def Find2(str2):
    word = str1.split()
    res2 = []
    for item in word:
        if item.find("https:") == 0 or item.find("http:") == 0:
            res2.append(item)
    return res2


str1 = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'

print('Urls:', Find2(str1))
