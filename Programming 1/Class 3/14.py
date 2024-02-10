def calculate_profit_loss(cost_price, selling_price):
    if selling_price > cost_price:
        profit = selling_price - cost_price
        return f"Profit: ${profit:.2f}"
    elif selling_price < cost_price:
        loss = cost_price - selling_price
        return f"Loss: ${loss:.2f}"
    else:
        return "No Profit, No Loss"

# Input from the user
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

result = calculate_profit_loss(cost_price, selling_price)
print(result)
