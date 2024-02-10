def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

def main():
    try:
        # Take input from the user
        input_str = input("Enter integers separated by spaces: ")
        input_list = [int(x) for x in input_str.split()]

        # Find duplicates
        duplicate_values = find_duplicates(input_list)

        # Display the result
        if duplicate_values:
            print("Duplicate values:", duplicate_values)
        else:
            print("No duplicate values found.")

    except ValueError:
        print("Error: Please enter valid integers separated by spaces.")

if __name__ == "__main__":
    main()
