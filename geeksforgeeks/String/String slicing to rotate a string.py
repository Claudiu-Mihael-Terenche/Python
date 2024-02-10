from collections import deque

# Function to rotate string left and right by d length

def rotate(str1, d1):

	# slice string in two parts for left and right
	Lfirst = str1[0 : d1]
	Lsecond = str1[d1 :]
	Rfirst = str1[0 : len(str1)-d1]
	Rsecond = str1[len(str1)-d1 : ]

	# now concatenate two parts together
	print('Left Rotation:', (Lsecond + Lfirst) )
	print('Right Rotation:', (Rsecond + Rfirst))

if __name__ == '__main__':
	str1 = 'GeeksforGeeks'
	d1 = 2
	rotate(str1, d1)

# Version 2

def rotate_string(str2, d2):
	deq = deque(str2)
	if d2 > 0:
		deq.rotate(-d2)
	else:
		deq.rotate(abs(d2))
	return ''.join(deq)

str2 = 'GeeksforGeeks'
d2 = 2

left_rotated = rotate_string(str2, d2)
right_rotated = rotate_string(str2, -d2)

print('Left rotation:', left_rotated)
print('Right rotation:', right_rotated)
