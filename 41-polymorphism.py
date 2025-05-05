# Polymorphism is used to generalizing functions
class Dog:
    def eat(self):
        print('dog is eating')

class Cat:
    def eat(self):
        print('cat is eating')

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()