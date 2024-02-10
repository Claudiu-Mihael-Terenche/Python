num_lines = int(input("Enter the number of lines: "))

# Print the first pattern
for i in range(num_lines, 0, -1):
    spaces = " " * (num_lines - i)
    stars = "* " * i
    print(spaces + stars)

# Print a blank line
print()

# Print the second pattern
for i in range(1, num_lines + 1):
    spaces = " " * (num_lines - i)
    stars = "* " * i
    print(spaces + stars)
