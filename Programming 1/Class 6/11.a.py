# Get the number of lines from user input
n = int(input("Enter the number of lines: "))

# Loop from 1 to n
for i in range(1, n+1):
  # Print the numbers from n-i+1 to n in each line
  for j in range(n-i+1, n+1):
    print(j, end="")
  # Print a new line after each iteration
  print()
