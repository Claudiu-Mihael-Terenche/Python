class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('talk')


John = Person("John Smith")
print(John.name)
John.talk()
