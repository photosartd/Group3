from abc import ABC, abstractmethod


# ABC - Abstract Base Class
class Shape(ABC):
    def __init__(self):
        print('Im Shape!')
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__()
        print('Im rectangle!')
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

    def perimeter(self):
        return 4 * self.a

r = Square(4)
print(r.perimeter())
