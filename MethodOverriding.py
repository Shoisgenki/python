#ability of a object oriented programming language to allow a subclass to provide a
#specific implementation of a method that is already provided in it's parent class

class Animal:
    def eat(self):
        print("This animal is eating...")


class Deer(Animal):
    def eat(self):
        print("This deer is eating forbs...")


deer = Deer()

deer.eat()