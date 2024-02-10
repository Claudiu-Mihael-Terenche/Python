def find_common_elements(array1, array2):
    common_elements = set(array1) & set(array2)
    return list(common_elements)

def main():
    # Input for the first array
    array1 = list(map(int, input("Enter elements of the first array (space-separated): ").split()))

    # Input for the second array
    array2 = list(map(int, input("Enter elements of the second array (space-separated): ").split()))

    # Find and print common elements
    common_elements = find_common_elements(array1, array2)

    if common_elements:
        print("Common elements:", common_elements)
    else:
        print("No common elements found.")

if __name__ == "__main__":
    main()
