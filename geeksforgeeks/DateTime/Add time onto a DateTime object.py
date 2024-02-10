import datetime

date_and_time = datetime.datetime(2021, 8, 22, 11, 2, 5)

print('Original time:')
print(date_and_time)

time_change = datetime.timedelta(days=3, hours=14, minutes=2, seconds=10)
new_time = date_and_time + time_change

print('Changed time:')
print(new_time)

'''
# Python3 code to illustrate the addition of time onto the datetime object

# importing datetime
import datetime

# initializing a date and time
date_and_time = datetime.datetime(2021, 8, 22, 11, 2, 5)

print('Original time:')
print(date_and_time)

# calling the timedelta() function and adding 2 minutes and 10 seconds
time_change = datetime.timedelta(days=3, hours=14, minutes=2, seconds=10)
new_time = date_and_time + time_change

print('Changed time:') # printing the new datetime object
print(new_time)

'''
