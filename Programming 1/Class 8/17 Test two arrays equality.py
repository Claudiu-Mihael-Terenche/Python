def are_arrays_equal(array1, array2):
    return array1 == array2

def main():
    # Taking user input for the first array
    input_str = input("Enter elements of the first array separated by spaces: ")
    array1 = list(map(int, input_str.split()))

    # Taking user input for the second array
    input_str = input("Enter elements of the second array separated by spaces: ")
    array2 = list(map(int, input_str.split()))

    # Testing the equality of the arrays
    if are_arrays_equal(array1, array2):
        print("The arrays are equal.")
    else:
        print("The arrays are not equal.")

if __name__ == "__main__":
    main()
