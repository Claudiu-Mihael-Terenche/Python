num_lines = int(input("Enter the number of lines: "))

# Print the upper part of the pattern
for i in range(1, num_lines + 1):
    spaces = " " * (num_lines - i)
    numbers = "".join(str(j % 10) for j in range(i, 0, -1))
    line = spaces + numbers + numbers[-2::-1]
    print(line)

# Print the lower part of the pattern
for i in range(num_lines - 1, 0, -1):
    spaces = " " * (num_lines - i)
    numbers = "".join(str(j % 10) for j in range(i, 0, -1))
    line = spaces + numbers + numbers[-2::-1]
    print(line)
