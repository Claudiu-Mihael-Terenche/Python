def remove_element(arr, element):
    if element in arr:
        arr.remove(element)
        print(f"Element {element} removed successfully.")
    else:
        print(f"Element {element} not found in the array.")

def main():
    # Taking array input from the user
    try:
        input_str = input("Enter elements of the array separated by spaces: ")
        arr = [int(x) for x in input_str.split()]
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return

    # Taking the element to be removed from the user
    try:
        element_to_remove = int(input("Enter the element to remove: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Removing the element from the array
    remove_element(arr, element_to_remove)

    # Displaying the updated array
    print("Updated array:", arr)

if __name__ == "__main__":
    main()
