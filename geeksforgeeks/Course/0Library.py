# Python program to illustrate functions

def hello():
	print('hello')
	print('hello again')


hello() # calling function

# Python program to illustrate a simple for loop

for step in range(5):
	print(step)

# iteration by for loop on range

for num in range(0, 10):
	print(num)

class Dog:
	attr1 = 'mammal'
	attr2 = 'dog'

	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)

Rodger = Dog()
print(Rodger.attr1)
Rodger.fun()

# Python program to swap two variables in a single line

x = 5; y = 10

x, y = y, x

print('After swapping values of x and y are', x, y)
