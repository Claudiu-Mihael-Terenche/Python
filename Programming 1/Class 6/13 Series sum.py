def series_sum(n):
    result = 0
    current_term = 1

    for _ in range(n):
        result += current_term
        current_term = current_term * 10 + 1

    return result

# Input the number of terms
n = int(input("Enter the number of terms: "))

# Calculate and print the sum of the series
sum_of_series = series_sum(n)
print(f"The sum of the series is: {sum_of_series}")

