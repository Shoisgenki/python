#where a derived class inherits another derived class

class Organism:
    alive = True


class Animal(Organism):
    def eat(self):
        print("This animal is eating...")

    def sleep(self):
        print("This animal is sleeping...")


class Dog(Animal):
    def bark(self):
        print("This dog is barking...")


dog = Dog()

print(dog.alive)
dog.eat()
dog.sleep()
dog.bark()
