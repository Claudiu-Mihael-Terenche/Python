task_time = int(input('Input the time spent to complete the task: '))

if task_time <= 3:
    print('Highly efficient worker')
elif task_time <= 4:
    print('The increase in speed is required')
elif task_time <= 5:
    print('Training required')
else:
    print('The worker is fired')
