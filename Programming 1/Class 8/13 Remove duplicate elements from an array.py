def remove_duplicates(arr):
    # Using a set to store unique elements
    unique_elements = set()

    # Using a list to maintain the order of elements
    result = []

    for element in arr:
        if element not in unique_elements:
            # Add to the result list if not already present
            result.append(element)
            unique_elements.add(element)

    return result


def main():
    try:
        # Taking input from the user
        input_array = input("Enter elements of the array separated by spaces: ")

        # Converting the input string to a list of integers
        array = list(map(int, input_array.split()))

        # Removing duplicates
        result_array = remove_duplicates(array)

        # Printing the result
        print("Array after removing duplicates:", result_array)

    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")


if __name__ == "__main__":
    main()
