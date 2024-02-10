from datetime import datetime

time1 = datetime.now().time()
time2 = datetime.now().strftime('%H:%M:%S')

print('Current time =\n', time1, '\n or\n' ,time2)
