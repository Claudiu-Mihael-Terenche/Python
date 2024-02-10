# Initialize the first two Fibonacci numbers
fibonacci_sequence = [0, 1]

# Generate Fibonacci numbers until the last number is less than or equal to 300
while fibonacci_sequence[-1] <= 300:
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)

# Print the Fibonacci numbers
for number in fibonacci_sequence[:-1]:  # Exclude the last number greater than 300
    print(number)
