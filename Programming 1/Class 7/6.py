import math

a = int(input('Input the length of the first side of the triangle (a): '))
b = int(input('Input the length of the second side of the triangle (b): '))
c = int(input('Input the length of the third side of the triangle (c): '))

perimeter = a + b + c
s = perimeter / 2
radicand = s * abs((s - a)) * abs((s - b)) * abs((s - c))
area = math.sqrt(radicand)

print('The area of your triangle is ', area)
