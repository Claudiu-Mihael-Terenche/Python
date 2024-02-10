def print_multiplication_table():
    # Print the header row
    print("   |", end="")
    for i in range(1, 11):
        print(f"{i:4}", end="")
    print("\n" + "-" * 45)

    # Print the table
    for i in range(1, 11):
        print(f"{i:2} |", end="")
        for j in range(1, 11):
            result = i * j
            print(f"{result:4}", end="")
        print()

# Call the method to print the multiplication table
print_multiplication_table()
