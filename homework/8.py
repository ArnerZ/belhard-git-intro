from abc import abstractmethod
class Point:
    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y

class Line:
    def __init__(self, x_1 : float, y_1 : float, x_2 : float, y_2 : float):
        self.point_1 = Point(x_1, y_1)
        self.point_2 = Point(x_2, y_2)
    def lenght(self,line):
        self.line = line
        return line((self.point_1.x-self.point_2.x)**2+(self.point_1.y-self.point_2.y)**2)

class Shape(Line): 
    def area(self):
        pass
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, x_1, y_1, x_2, y_2):
        super().__init__(x_1, y_1, x_2, y_2)
        self.side = super().lenght()
    def area(self) -> float:
        return self.side ** 2
    def perimeter(self) -> float:
        return self.side * 4


class Rect(Shape):
    def __init__(self, h, l):
        self.h = h
        self.l = l
    def area(self) -> float:
        return self.h * self.l
    def perimeter(self) -> float:
        return 2 * (self.h + self.l)
        
class Cube(Square):
    def __init__(self, x_1, y_1, x_2, y_2):
        super().__init__(x_1, y_1, x_2, y_2)
    def volume(self) -> float:
        return self.side ** 3   

cube = Cube(10, 5, 2, 8)
print(f"Объем куба = {cube.volume}")
print(f"Сторона куба = {cube.side}")
print(f"Площадь поверхности куба = {cube.area}")
print(f"Периметр стороно куба = {cube.perimeter}")

rect = Rect(10, 5)

print(f"Периметр прямоугольника = {rect.perimeter}")
print(f"Площадь прямоугольника = {rect.area}")