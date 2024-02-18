# Python3 code to split strings on prefix occurrence using loop + startswith()
list1 = ['geeksforgeeks', 'best', 'geeks', 'and', 'geeks', 'love', 'CS']
pref1 = 'geek'

res = []
for item in list1:
    if item.startswith(pref1):  # checking for prefix
        res.append([item])  # if pref found, start new list
    else:
        res[-1].append(item)  # else append in current list

print('Prefix split list:', res)
