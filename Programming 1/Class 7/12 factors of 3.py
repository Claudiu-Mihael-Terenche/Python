def display_factors_of_three(num):
    factors_of_three = [i for i in range(1, num + 1) if num % i == 0 and i % 3 == 0]

    print(f"The factors of {num} that are divisible by 3 are: {factors_of_three}")


# Example usage:
number = abs(int(input('Input your number: ')))  # Replace with your desired integer
display_factors_of_three(number)
