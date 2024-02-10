from datetime import datetime

day_num = '339'

day_num.rjust(3 + len(day_num), '0')

year = '2020'

res1 = datetime.strptime(year + '-' + day_num, '%Y-%j').strftime('%m-%d-%Y')

print('Resolved date:', res1)

from datetime import datetime, date, timedelta

strt_date = date(int(year), 1, 1)

res2 = (strt_date + timedelta(days=int(day_num) - 1)).strftime('%m-%d-%Y')

print('Resolved date:', res2)

'''
# Python3 code to demonstrate working of
# Convert day number to date in particular year
# Using datetime.strptime()
from datetime import datetime

day_num = '339' # initializing day number

# print day number
# print("The day number : " + str(day_num))

# adjusting day num

day_num.rjust(3 + len(day_num), '0')

year = '2020' # initialize year

# converting to date
res1 = datetime.strptime(year + '-' + day_num, '%Y-%j').strftime('%m-%d-%Y')

print('Resolved date:', res1)

# Python3 code to demonstrate working of
# Convert day number to date in particular year
# Using datetime.strptime()
from datetime import datetime, date, timedelta

# initializing day number
# day_num = "339"

# print day number
# print("The day number : " + str(day_num))

# adjusting day num
# day_num = day_num.rjust(3 + len(day_num), '0')

# Initialize year
# year = "2020"

# Initializing start date

strt_date = date(int(year), 1, 1)

# converting to date
res2 = (strt_date + timedelta(days=int(day_num) - 1)).strftime('%m-%d-%Y')

print('Resolved date:', res2)

'''
