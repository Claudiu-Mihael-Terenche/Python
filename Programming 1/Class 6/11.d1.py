def print_pattern(num_lines):
    for i in range(num_lines, 0, -1):
        # Print spaces for indentation
        print(" " * (num_lines - i), end="")

        # Print asterisks for the current line
        for j in range(i):
            print("*", end=" ")

        # Move to the next line
        print()

# Get the number of lines from the user
num_lines = int(input("Enter the number of lines: "))

# Print the pattern
print_pattern(num_lines)
