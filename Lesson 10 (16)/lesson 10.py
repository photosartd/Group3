class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'x: {self.x}\n' + f'y: {self.y}'

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)


class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

    def bounding_box(self):
        pass

    @classmethod
    def from_file(cls, filename):
        pass

    @staticmethod
    def to_file(filename):
        pass


class Rectangular(Shape):
    def __init__(self, bottom_left: Point, top_right: Point):
        super().__init__()
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.top_left = Point(bottom_left.x, top_right.y)
        self.bottom_right = Point(top_right.x, bottom_left.y)

    def _get_a_b(self):
        a = self.top_right.x - self.bottom_left.x
        b = self.top_right.y - self.bottom_left.y
        return a, b

    def area(self):
        a, b = self._get_a_b()
        return a * b

    def perimeter(self):
        a, b = self._get_a_b()
        return 2 * (a + b)

    def bounding_box(self):
        return self

    @staticmethod
    def to_file(rect, filename: str='rect.txt'):
        with open(filename, 'w') as f:
            lines = [
                f'{rect.bottom_left.x} {rect.bottom_left.y}\n',
                f'{rect.top_right.x} {rect.top_right.y}'
            ]
            f.writelines(lines)

    @classmethod
    def from_file(cls, filename: str):
        with open(filename, 'r') as f:
            x1, y1 = map(int, f.readline().split())
            x2, y2 = map(int, f.readline().split())
        return cls(Point(x1, y1), Point(x2, y2))

    def __str__(self):
        return f'Bottom left: \n{self.bottom_left}\
        \nTop right: \n{self.top_right}'


class Square(Rectangular):
    def __init__(self, bottom_left: Point, top_right: Point):
        a = top_right.x - bottom_left.x
        b = top_right.y - bottom_left.y
        if a != b:
            raise Exception('This is not a square')
        super(Square, self).__init__(bottom_left, top_right)

p1 = Point(1, 1)
p2 = Point(3, 4)
#rect = Rectangular(p1, p2)
#print(rect.area())
#print(rect.perimeter())
#Rectangular.to_file(rect)
rect = Rectangular.from_file('rect.txt')
print(rect)
print(type(rect))

sq = Square(Point(), Point(4,4))




