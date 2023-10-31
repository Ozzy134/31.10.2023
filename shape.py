class Shape:

    def __init__(self, name, color):
        self.name = name
        self.color = color

class Circle(Shape):

    def __init__(self, color, radius):
        super().__init__(radius, color=color)
        self.radius = radius

    def aria(self):
        x = self.radius * self.radius * 3.14
        print()