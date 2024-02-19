list1 = [1, 4, 9, 10, 19]
matrix1 = [[5, 6, 8], [8, 5, 3], [9, 10, 3]]

res_list = list(map(str, list1))

res_matrix = list(map(lambda sub: list(map(str, sub)), matrix1))

print('The list after type casting is:', res_list)
print('The matrix after type casting is:', res_matrix)

'''
# Python3 code to demonstrate working of
# Type casting whole List and Matrix
# using map() + list comprehension

# helper function to type cast list
def cast_list(test_list, data_type):
    return list(map(data_type, test_list))


# helper function to type cast Matrix
def cast_matrix(test_matrix, data_type):
    return list(map(lambda sub: list(map(data_type, sub)), test_matrix))

list1 = [1, 4, 9, 10, 19]

matrix1 = [[5, 6, 8], [8, 5, 3], [9, 10, 3]]

# printing original list
print("The original list is : " + str(test_list))

# printing original matrix
print("The original Matrix is : " + str(test_matrix))

# Type casting whole List and Matrix
# using map() + list comprehension
res_list = cast_list(test_list, str)
res_matrix = cast_matrix(test_matrix, str)

res_list = list(map(str, list1))
res_matrix = list(map(lambda sub: list(map(str, sub)), matrix1))

print('The list after type casting is:', res_list)
print('The matrix after type casting is:', res_matrix)
'''
