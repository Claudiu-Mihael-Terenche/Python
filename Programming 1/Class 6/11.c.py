num_lines = int(input("Enter the number of lines: "))

for i in range(1, num_lines + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
