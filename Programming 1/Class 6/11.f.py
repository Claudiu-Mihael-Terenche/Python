num_lines = int(input("Enter the number of lines: "))

current_number = 1

for i in range(1, num_lines + 1):
    for j in range(i):
        print(current_number, end=" ")
        current_number += 1
    print()
