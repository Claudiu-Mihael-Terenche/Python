from datetime import date
from datetime import timedelta

today = date.today()

print('Today is:', today)

yesterday = today - timedelta(days=1)
print('Yesterday was:', yesterday)

n = int(input('How many days ago do you want to know what date was? '))
nDaysAgoTheDateWas = today - timedelta(days=n)
print(n, 'days ago the date was:', nDaysAgoTheDateWas)

print('Current year:', today.year)
print('Current month:', today.month)
print('Current day:', today.day)

'''
# Python program to get
# Yesterday's date


# Import date and timedelta class
# from datetime module
from datetime import date
from datetime import timedelta

today = date.today() # get today's date

print('Today is:', today)

yesterday = today - timedelta(days=1) # yesterday date 3 days ago days = 3
print('Yesterday was:', yesterday)

n = int(input('How many days ago do you want to know what date was? '))
nDaysAgoTheDateWas = today - timedelta(days=n)
print(n, 'days ago the date was:', nDaysAgoTheDateWas)

print('Current year:', today.year) # fetching the current year, month and day of today
print('Current month:', today.month)
print('Current day:', today.day)
'''
