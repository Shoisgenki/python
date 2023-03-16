#super() = function used to give access to methods of
#parent class
           #returns a temporary object of a parent class when used

class Rect:

    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rect):

    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length*self.width


class Cube(Rect):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height


cube = Cube(3, 5, 9)

print(cube.volume())