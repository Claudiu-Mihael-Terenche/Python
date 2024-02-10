price = 1_000_000
has_good_credit = True
if has_good_credit:
    down_payment = 10 / 100 * price
else:
    down_payment = 20 / 100 * price
print(f"Your down payment is: ${down_payment}")
