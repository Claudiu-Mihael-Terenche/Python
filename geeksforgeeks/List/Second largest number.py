# Python program to find second largest number in a list using sort() or sorted()

list1 = [2, 10, 20, 20, 5, 45, 7, 45, 6, 45, 8, 99, 4, 99, 37, 11]

list2 = list(set(list1)) # removing duplicates from the list

res1 = sorted(list2)[-2]

print('Second largest element is:', res1) # printing the second last element

res2 = list2.sort() # sorting the list

res2 = list2[-2]

print('Second largest element is:', res2) # print second maximum element
