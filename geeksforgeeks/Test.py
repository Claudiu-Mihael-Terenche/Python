def hello():
    print('hello')
    print('hello again')


hello()

for step in range(5):
    print(step)

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
