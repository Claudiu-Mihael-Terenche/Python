def display_matrix(n):
    if n <= 0:
        print("Please enter a positive integer for the matrix size.")
        return

    # Generate the matrix based on the given pattern
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0 or (i - j) % 3 == 0:
                matrix[i][j] = 1

    # Display the matrix
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

# Input a number
n = int(input("Input a number: "))
display_matrix(n)
