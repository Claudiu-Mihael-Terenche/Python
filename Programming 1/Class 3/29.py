delay = int(input('Input the numbers of day are you late: '))

if delay < 5:
    print('Fine is $0.5')
elif delay <= 10:
    print('Fine is $3')
elif delay < 30:
    print('Fine is $5')
else:
    print('Your membership was cancelled')
