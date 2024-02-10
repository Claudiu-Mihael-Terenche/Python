def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for value in arr:
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)

    return duplicates

def main():
    # Take input from the user
    n = int(input("Enter the number of elements in the array: "))
    array = []

    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        array.append(element)

    # Find and print duplicate values
    duplicate_values = find_duplicates(array)

    if duplicate_values:
        print("Duplicate values in the array are:", ', '.join(duplicate_values))
    else:
        print("No duplicate values found in the array.")

if __name__ == "__main__":
    main()
