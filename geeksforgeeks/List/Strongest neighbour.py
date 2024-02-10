# Define a function for finding the maximum for adjacent pairs in the array

def maximumAdjacent(arr1, n):
    arr2 = [] # array to store the max value between adjacent pairs
    for num in range(1, n): # iterate from 1 to n - 1
        r = max(arr1[num], arr1[num - 1]) # find max value between adjacent pairs gets stored in r
        arr2.append(r)  # add element
    for num in arr2: # printing the elements
        print(num, end=' ')


if __name__ == '__main__':

    n = 7

    arr1 = [1, 2, 2, 8, 3, 4, 5]


    maximumAdjacent(arr1, n)
