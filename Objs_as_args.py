class Car:

    color = None

class Bike:

    color = None

def change_color(x, y):  #just a function where we insert objects as args

    x.color = y


bentley = Car()
ducatti = Bike()

change_color(bentley, "Red")
change_color(ducatti, "Black")

print(bentley.color)
print(ducatti.color)

