def separate_zeros_ones(arr):
    # Count the number of zeros
    count_zeros = arr.count(0)

    # Fill the array with zeros on the left
    separated_array = [0] * count_zeros

    # Fill the remaining part of the array with ones
    separated_array.extend([1] * (len(arr) - count_zeros))

    return separated_array


def main():
    # Take user input for a random array of 0s and 1s
    input_str = input("Enter a random array of 0s and 1s (e.g., 101001): ")

    # Convert the input string to a list of integers
    try:
        user_array = [int(bit) for bit in input_str]
    except ValueError:
        print("Invalid input. Please enter only 0s and 1s.")
        return

    # Separate 0s on the left and 1s on the right
    separated_array = separate_zeros_ones(user_array)

    # Print the separated array
    print("Separated Array:", separated_array)


if __name__ == "__main__":
    main()
