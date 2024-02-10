def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i + 1}, {j + 1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))

        print("Enter elements for the first matrix:")
        matrix1 = input_matrix(rows, cols)

        print("\nEnter elements for the second matrix:")
        matrix2 = input_matrix(rows, cols)

        result_matrix = add_matrices(matrix1, matrix2)

        print("\nThe sum of the matrices is:")
        print_matrix(result_matrix)

    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
