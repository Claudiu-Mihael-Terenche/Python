def generate_pentagonal_numbers(n):
    pentagonal_numbers = []
    for i in range(1, n + 1):
        pentagonal_number = i * (3 * i - 1) // 2
        pentagonal_numbers.append(pentagonal_number)
    return pentagonal_numbers

def display_pentagonal_numbers():
    n = 50  # You can change this value to generate a different number of pentagonal numbers
    pentagonal_numbers = generate_pentagonal_numbers(n)

    print("First 50 Pentagonal Numbers:")
    for i, num in enumerate(pentagonal_numbers, 1):
        print(f"{i}: {num}")

# Call the method to display the first 50 pentagonal numbers
display_pentagonal_numbers()
