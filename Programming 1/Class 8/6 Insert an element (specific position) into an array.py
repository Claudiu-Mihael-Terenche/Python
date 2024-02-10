def insert_element(arr, element, position):
    """
    Function to insert an element into an array at a specific position.

    Parameters:
    - arr: The input array.
    - element: The element to be inserted.
    - position: The position at which the element should be inserted.

    Returns:
    - The modified array after insertion.
    """
    arr.insert(position, element)
    return arr

def main():
    # Get array input from the user
    try:
        arr = list(map(int, input("Enter the array elements (space-separated): ").split()))
    except ValueError:
        print("Please enter valid integers.")
        return

    # Get element to insert
    try:
        element = int(input("Enter the element to insert: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Get position to insert
    try:
        position = int(input("Enter the position to insert (0-based index): "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Insert the element at the specified position
    modified_array = insert_element(arr, element, position)

    # Display the modified array
    print("Modified Array:", modified_array)

if __name__ == "__main__":
    main()
