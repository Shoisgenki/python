# Class can inherit attributes and methods from another class

class Animal:
    alive = True

    def eat(self):
        print("This animal is eating...")

    def sleep(self):
        print("This animal is sleeping...")


class Deer(Animal):
    def run(self):
        print("This deer is running")


class Bear(Animal):
    def search(self):
        print("This bear is searching")


class Dog(Animal):
    def play(self):
        print("This dog is playing")


deer = Deer()
bear = Bear()
dog = Dog()

print(deer.alive)
bear.search()