# prevents a user from creating object of that class
# compels a user to override abstract methods in a child class

#abstract class = a class which contains one or more abstract methods.
#abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod as muji


class Vehicle(ABC):

    @muji
    def go(self):
        pass

    @muji
    def stop(self):
        pass


class Car(Vehicle):  # if you inherit an abstract class#
                                                       #
    def go(self):                                      #
        print("This car is moving...")                 #
                                                       #
    def stop(self):                                    #
        print("This car has stopped...")               #
                                                       #
                                                       #
class Bike(Vehicle): # all the methods must override   #

    def go(self):
        print("This bike is moving...")

    def stop(self):
        print("This bike has stopped...")


bike = Bike()
car = Car()


#bike.go()
car.go()
