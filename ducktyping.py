# concept where the class of an object is less important
# than the methods/attributes. Class type is not checked if minimum
# methods/attributes are present


class Duck:
    def walk(self):
        print("This duck is walking...")

    def talk(self):
        print("This duck is quacking...")


class Chicken:
    def walk(self):
        print("This chicken is walking...")

    def talk(self):
        print("This chicken is clucking...")


class Person:
    def catch(self, x):
        x.walk()
        x.talk()
        print("You caught the critter!")


chick = Chicken()
duck = Duck()
person = Person()

person.catch(duck)

