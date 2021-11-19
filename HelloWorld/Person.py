#import from converters module
import converters
#import only the lbs_to_kgs function
from converters import lbs_to_kgs

class Mammal:
    def walk(self):
        print("walk")
class Person(Mammal):
    #Constructor
    def __init__(self, name):
        self.name=name
    def talk(self):
        print(f'Hi. I am {self.name}!')

class Dog(Mammal):
    #Constructor
    def __init__(self, name):
        self.name=name
    def bark(self):
        print('woof!')


p1 = Person("Ralf Pfeiffer")
p1.talk()
p2 = Person("John  Smith")
p2.walk()
p2.talk()

d1 = Dog('Bisquit')
d1.walk()
d1.bark()

#using the converters module...
print(converters.lbs_to_kgs(225))
print(lbs_to_kgs(200))




