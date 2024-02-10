while True:
    weight = int(input('Weight: '))
    unit = input('(L)bs or (K)g: ')

    if unit.upper() == 'L':
        converted = weight * 0.45
        print(f'You are {converted} kilos')
        break
    elif unit.upper() == 'K':
        converted = weight / 0.45
        print(f'You are {converted} pounds')
        break
    else:
        print('You need to choose (L)bs or (K)g. Please try again.')
