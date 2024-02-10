# Input values
principal = 1000  # Initial investment amount
interest_rate = 0.0625  # Annual interest rate (6.25%)
num_of_years = int(input('Input the number of years: '))  # Number of years for the investment

# Calculate the profit using the compound interest formula
future_value = principal * (1 + interest_rate) ** num_of_years
profit = future_value - principal

# Display the result
print(f"Initial investment: ${principal:.2f}")
print(f"Annual interest rate: {interest_rate * 100:.2f}%")
print(f"Number of years: {num_of_years}")
print(f"Future value: ${future_value:.2f}")
print(f"Profit: ${profit:.2f}")
