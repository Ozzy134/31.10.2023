class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        return 'Рисуем фигуру'

class Line(Figure):
    def draw(self):
        return 'Рисуем линию'

class Rect(Figure):
    def __init__(self, coords, width, color, side):
        super().__init__(coords, width, color)
        self.side = side

    def draw(self):
        return 'Рисуем прямоугольник'

    def sqare(self):
        return 'Находим площадь'

class Ellips(Figure):
    def draw(self):
        return 'Рисуем элипс'

def try_ti_draw(obj):
    print(obj.draw())


f = Figure([1,1,5,6,8,7,5,9,5,4], 3, 'black')
print(f.coords)
print(f.draw())
l = Line([1,1,5,5], 2, 'red')
print(f'{l.draw()} толщиной {l.width} и цветом {l.color}')
r = Rect([1,1,6,6], 6, 'yellow', '16')
print(r.sqare())
try_ti_draw(f)
