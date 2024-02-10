from operator import length_hint
import time

list1 = [1, 4, 5, 7, 8]

start_time_naive = time.time() # finding length of list using loop
counter = 0
for num in list1:
	counter = counter + 1
end_time_naive = str(time.time() - start_time_naive) # incrementing counter

start_time_len = time.time() # finding length of list using len()
list_len = len(list1)
end_time_len = str(time.time() - start_time_len)

start_time_hint = time.time() # finding length of list using length_hint()
list_len_hint = length_hint(list1)
end_time_hint = str(time.time() - start_time_hint)

print('Time taken using naive method is:', end_time_naive)
print('Time taken using len() is:', end_time_len)
print('Time taken using length_hint() is:', end_time_hint)
