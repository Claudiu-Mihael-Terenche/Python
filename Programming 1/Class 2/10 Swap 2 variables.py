def main():
    # Get input from the user
    num1 = input("Enter the first variable: ")
    num2 = input("Enter the second variable: ")

    # Display the original values
    print("Original values:")
    print("First variable:", num1)
    print("Second variable:", num2)

    # Swap the variables using a temporary variable
    temp = num1
    num1 = num2
    num2 = temp

    # Display the swapped values
    print("\nAfter swapping:")
    print("First variable:", num1)
    print("Second variable:", num2)

if __name__ == "__main__":
    main()
