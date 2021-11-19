class Person:
    #Constructor
    def __init__(self, name):
        self.name=name
    def talk(self):
        print('talk')

talk()
person = Person("Ralf Pfeiffer")

print(person.name)






