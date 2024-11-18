import math

class Figure:
    def area(self):
        raise NotImplementedError()

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return "Фігура"

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Прямокутник: ширина = {self.width}, висота = {self.height}"

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Коло: радіус = {self.radius}"

class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Прямокутний трикутник: основа = {self.base}, висота = {self.height}"

class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def __str__(self):
        return f"Трапеція: основа1 = {self.base1}, основа2 = {self.base2}, висота = {self.height}"

rect = Rectangle(30, 18)
circle = Circle(7)
triangle = RightTriangle(6, 3)
trapezoid = Trapezoid(5, 9, 6)

print(f"Площа прямокутника: {int(rect)}")
print(f"Площа кола: {int(circle)}")
print(f"Площа прямокутного трикутника: {int(triangle)}")
print(f"Площа трапеції: {int(trapezoid)}")

print(rect)
print(circle)
print(triangle)
print(trapezoid)


class Shape:
    def __init__(self, filename):
        self.filename = filename

    def show(self):
        raise NotImplementedError("Метод 'show' повинен бути реалізований.")

    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.__str__())

    def load(self):
        with open(self.filename, 'r') as file:
            content = file.read()
            self.from_string(content)

    def from_string(self, data):
        raise NotImplementedError("Метод 'from_string' повинен бути реалізований.")

class Square(Shape):
    def __init__(self, filename, top_left_x, top_left_y, side_length):
        super().__init__(filename)
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.side_length = side_length

    def show(self):
        return f"Square: Top Left({self.top_left_x}, {self.top_left_y}), Side Length: {self.side_length}"

    def __str__(self):
        return f"Square,{self.top_left_x},{self.top_left_y},{self.side_length}\n"

    def from_string(self, data):
        _, self.top_left_x, self.top_left_y, self.side_length = data.strip().split(',')
        self.top_left_x = int(self.top_left_x)
        self.top_left_y = int(self.top_left_y)
        self.side_length = int(self.side_length)


class Rectangle(Shape):
    def __init__(self, filename, top_left_x, top_left_y, width, height):
        super().__init__(filename)
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.width = width
        self.height = height

    def show(self):
        return f"Rectangle: Top Left({self.top_left_x}, {self.top_left_y}), Width: {self.width}, Height: {self.height}"

    def __str__(self):
        return f"Rectangle,{self.top_left_x},{self.top_left_y},{self.width},{self.height}\n"

    def from_string(self, data):
        _, self.top_left_x, self.top_left_y, self.width, self.height = data.strip().split(',')
        self.top_left_x = int(self.top_left_x)
        self.top_left_y = int(self.top_left_y)
        self.width = int(self.width)
        self.height = int(self.height)


class Circle(Shape):
    def __init__(self, filename, center_x, center_y, radius):
        super().__init__(filename)
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def show(self):
        return f"Circle: Center({self.center_x}, {self.center_y}), Radius: {self.radius}"

    def __str__(self):
        return f"Circle,{self.center_x},{self.center_y},{self.radius}\n"

    def from_string(self, data):
        _, self.center_x, self.center_y, self.radius = data.strip().split(',')
        self.center_x = int(self.center_x)
        self.center_y = int(self.center_y)
        self.radius = int(self.radius)

class Ellipse(Shape):
    def __init__(self, filename, top_left_x, top_left_y, width, height):
        super().__init__(filename)
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.width = width
        self.height = height

    def show(self):
        return f"Ellipse: Top Left({self.top_left_x}, {self.top_left_y}), Width: {self.width}, Height: {self.height}"

    def __str__(self):
        return f"Ellipse,{self.top_left_x},{self.top_left_y},{self.width},{self.height}\n"

    def from_string(self, data):
        _, self.top_left_x, self.top_left_y, self.width, self.height = data.strip().split(',')
        self.top_left_x = int(self.top_left_x)
        self.top_left_y = int(self.top_left_y)
        self.width = int(self.width)
        self.height = int(self.height)

shapes = [
    Square("square.txt", 1, 1, 5),
    Rectangle("rectangle.txt", 2, 2, 4, 6),
    Circle("circle.txt", 3, 3, 2),
    Ellipse("ellipse.txt", 4, 4, 6, 3)
]
for shape in shapes:
    shape.save()

loaded_shapes = []
for shape in shapes:
    if isinstance(shape, Square):
        new_shape = Square(shape.filename, 0, 0, 0)
    elif isinstance(shape, Rectangle):
        new_shape = Rectangle(shape.filename, 0, 0, 0, 0)
    elif isinstance(shape, Circle):
        new_shape = Circle(shape.filename, 0, 0, 0)
    elif isinstance(shape, Ellipse):
        new_shape = Ellipse(shape.filename, 0, 0, 0, 0)

    new_shape.load()
    loaded_shapes.append(new_shape)
for shape in loaded_shapes:
    print(shape.show())














