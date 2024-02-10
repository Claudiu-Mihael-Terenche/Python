def is_value_in_array(arr, value):
    return value in arr


def main(raw_input=None):
    # Take input from the user to create an array
    try:
        # Python 2.x: input() is used for taking user input
        # Python 3.x: input() is used for taking user input
        input_string = input("Enter elements of the array separated by space: ")
    except NameError:
        input_string = raw_input("Enter elements of the array separated by space: ")

    # Convert the input string into a list of integers
    arr = list(map(int, input_string.split()))

    # Take the value to check from the user
    try:
        value = int(input("Enter the value to check in the array: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Check if the value is in the array
    if is_value_in_array(arr, value):
        print(f"The array {arr} contains the value {value}.")
    else:
        print(f"The array {arr} does not contain the value {value}.")


if __name__ == "__main__":
    main()
