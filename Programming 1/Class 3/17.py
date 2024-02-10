def calculate_bill(number_of_units):
    if number_of_units <= 50:
        Rs = 0.5
    elif number_of_units <= 150:
        Rs = 0.75
    elif number_of_units <= 250:
        Rs = 1.2
    else:
        Rs = 1.5


    bill = (number_of_units * Rs) * 1.2
    return bill

# Taking input for number_of_units
number_of_units = float(input('Input the number of units: '))

# Claculate and print the bill
bill = calculate_bill(number_of_units)
print('Your bill is:', bill)
