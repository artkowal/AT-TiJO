from abc import ABC, abstractmethod

class DrawableFigure(ABC):
    @abstractmethod
    def draw(self):
        pass


class Square(DrawableFigure):
    def __init__(self, a):
        self.a = a

    def draw(self):
        for _ in range(self.a):
            print(self.a * "o ")
        print()


class Triangle(DrawableFigure):
    def __init__(self, h):
        self.h = h

    def draw(self):
        for side in range(self.h):
            print((side + 1) * "o ")
        print()


class FigureDrawer:
    def draw(self, figure: DrawableFigure):
        figure.draw()


a = 5
h = 5

square = Square(a)
triangle = Triangle(h)

drawer = FigureDrawer()
drawer.draw(square)
drawer.draw(triangle)
