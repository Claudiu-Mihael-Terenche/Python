def calculate_total(item_price, lbs):
    return item_price * lbs

def main():
    # Item prices
    carrot_price = 2
    onion_price = 4
    meat_price = 10

    # Get customer input
    carrots_lbs = float(input('Enter the number of pounds of carrots: '))
    onions_lbs = float(input('Enter the number of pounds of onions: '))
    meat_lbs = float(input('Enter the number of pounds of meat: '))

    # Calculate subtotals for each item
    carrots_total = calculate_total(carrot_price, carrots_lbs)
    onions_total = calculate_total(onion_price, onions_lbs)
    meat_total = calculate_total(meat_price, meat_lbs)

    # Calculate total before tax
    total_before_tax = carrots_total + onions_total + meat_total

    # Ask for payment method
    payment_method = input('Enter payment method (Cash or Card): ').lower()

    if payment_method == 'card':
        # Apply 13% HST
        tax = total_before_tax * 0.13
        total_amount = total_before_tax + tax
    elif payment_method == 'cash':
        total_amount = total_before_tax
    else:
        print("Invalid payment method. Please enter 'Cash' or 'Card'.")
        return

    # Display the invoice
    print('\nInvoice:')
    print('========')
    print(f'Carrots: {carrots_lbs} lbs x ${carrot_price:.2f} / lb = ${carrots_total:.2f}')
    print(f'Onions: {onions_lbs} lbs x ${onion_price:.2f} / lb = ${onions_total:.2f}')
    print(f'Meat: {meat_lbs} lbs x ${meat_price:.2f} / lb = ${meat_total:.2f}')
    print(f'Total before tax: ${total_before_tax:.2f}')
    if payment_method == 'card':
        print(f'Tax (13% HST): ${tax:.2f}')
    print(f'Total amount to pay: ${total_amount:.2f}')

if __name__ == "__main__":
    main()
