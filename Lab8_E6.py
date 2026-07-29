#Example 6
#abstract class cant be instantiated

from abc import ABC,abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can mive and run")

class Snake(Animal):
    def move(self):
        print("I can Bark")
class Dog(animal):
    def move(self):
        print("I can Bark")

class Lion(Animal):
    def move(self):
        print("I can roar")

c.Animal()