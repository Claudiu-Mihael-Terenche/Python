from collections import deque


# Function to rotate string left and right by d length

def rotate(str01, d01):
    # slice string in two parts for left and right
    l_first = str01[0: d01]
    l_second = str01[d01:]
    r_first = str01[0: len(str1) - d01]
    r_second = str01[len(str1) - d01:]

    # now concatenate two parts together
    print('Left Rotation:', (l_second + l_first))
    print('Right Rotation:', (r_second + r_first))


if __name__ == '__main__':
    str1 = 'GeeksforGeeks'
    d1 = 2
    rotate(str1, d1)


# Version 2

def rotate_string(str02, d02):
    deq = deque(str02)
    if d02 > 0:
        deq.rotate(-d02)
    else:
        deq.rotate(abs(d02))
    return ''.join(deq)


str2 = 'GeeksforGeeks'
d2 = 2

left_rotated = rotate_string(str2, d2)
right_rotated = rotate_string(str2, -d2)

print('Left rotation:', left_rotated)
print('Right rotation:', right_rotated)
