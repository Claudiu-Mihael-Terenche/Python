def rearrange_array(arr):
    # Separate negative and positive integers
    negatives = [num for num in arr if num < 0]
    positives = [num for num in arr if num >= 0]

    # Concatenate the negative and positive integers
    arranged_array = negatives + positives

    return arranged_array

def main():
    # Take user input for the array of integers
    try:
        input_str = input("Enter integers separated by spaces: ")
        input_list = list(map(int, input_str.split()))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    # Rearrange the array and display the result
    result = rearrange_array(input_list)
    print("Rearranged Array:", result)

if __name__ == "__main__":
    main()
