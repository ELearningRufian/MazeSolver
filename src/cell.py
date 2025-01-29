from line import *
from window import *

class Cell:
    def __init__(self, p0, p1, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x0 = p0.x
        self._y0 = p0.y
        self._x1 = p1.x
        self._y1 = p1.y
        self._win = win

    def draw(self, cell_color):
        if self.has_left_wall:
            print("left:")
            print(((self._x0, self._y0),(self._x0, self._y1)))
            Line(Point(self._x0, self._y0), Point(self._x0, self._y1)).draw(self._win.canvas, cell_color)
        if self.has_top_wall:
            print("top:")
            print(((self._x1, self._y0),(self._x0, self._y0)))
            Line(Point(self._x1, self._y0), Point(self._x0, self._y0)).draw(self._win.canvas, cell_color)
        if self.has_right_wall:
            print("right:")
            print(((self._x1, self._y1),(self._x1, self._y0)))
            Line(Point(self._x1, self._y1), Point(self._x1, self._y0)).draw(self._win.canvas, cell_color)
        if self.has_bottom_wall:
            print("bottom:")
            print(((self._x0, self._y1),(self._x1, self._y1)))
            Line(Point(self._x0, self._y1), Point(self._x1, self._y1)).draw(self._win.canvas, cell_color)
