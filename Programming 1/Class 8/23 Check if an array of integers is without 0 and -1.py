def check_array(arr):
    return all(x != 0 and x != -1 for x in arr)

def main():
    try:
        # Take user input for array of integers
        input_str = input("Enter an array of integers separated by spaces: ")
        user_array = list(map(int, input_str.split()))

        # Check if the array is without 0 and -1
        result = check_array(user_array)

        # Output the result
        if result:
            print("The array does not contain 0 and -1.")
        else:
            print("The array contains 0 and/or -1.")

    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")

if __name__ == "__main__":
    main()
