def calculate_bill(value_before_discount):
    if value_before_discount < 100:
        discount_percentage = 0
    else:
        discount_percentage = 10


    discount = (discount_percentage / 100) * value_before_discount

    bill = value_before_discount - discount
    return bill

# Taking input for value
value_before_discount = float(input('Input the value of items: '))

# Calculate and print the bill
bill = calculate_bill(value_before_discount)
print(bill)
