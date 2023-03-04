#methodchaining = calling multiple methods sequentially

class Car:

    def turnOn(self):
        print("You start the engine...")
        return self

    def drive(self):
        print("You drive the car...")
        return self

    def brake(self):
        print("You hit the brakes...")
        return self

    def turnOff(self):
        print("You turn off the engine...")
        return self


class Corvette(Car):

    def drive(self):
        print("You drive the corvette...")
        return self


corvette = Corvette()


corvette\
    .turnOn()\
    .drive()\
    .brake()\
    .turnOff()
