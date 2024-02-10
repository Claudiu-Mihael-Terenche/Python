def calculate_future_value(investment_amount, interest_rate, years):
    # Convert interest rate to decimal
    interest_rate_decimal = interest_rate / 100.0

    # Calculate future value using the compound interest formula
    future_value = investment_amount * (1 + interest_rate_decimal / 12) ** (years * 12)

    return future_value

def main():
    # Input investment amount, interest rate, and number of years
    investment_amount = float(input("Input the investment amount: "))
    interest_rate = float(input("Input the rate of interest: "))
    years = int(input("Input number of years: "))

    # Print header
    print("Years    FutureValue")

    # Calculate and print future values for each year
    for year in range(1, years + 1):
        future_value = calculate_future_value(investment_amount, interest_rate, year)
        print(f"{year:2}       {future_value:.2f}")

if __name__ == "__main__":
    main()
