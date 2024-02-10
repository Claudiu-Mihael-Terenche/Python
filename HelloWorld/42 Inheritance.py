class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


John = Person('John Smith')
John.talk()

Bob = Person('Bob Smith')
Bob.talk()
