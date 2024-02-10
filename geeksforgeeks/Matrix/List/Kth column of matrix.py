# Python code to get Kth column of matrix using list slicing

list1 = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]

K = 2

res = [row[K] for row in list1]

print('The Kth column of matrix is:', res)
