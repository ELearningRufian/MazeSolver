from line import *
from window import *

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win

    def draw(self, p0, p1, cell_color):
        self._x0 = p0.x
        self._y0 = p0.y
        self._x1 = p1.x
        self._y1 = p1.y
        if self.has_left_wall:
            Line(Point(self._x0, self._y0), Point(self._x0, self._y1)).draw(self._win.canvas, cell_color)
        if self.has_top_wall:
            Line(Point(self._x1, self._y0), Point(self._x0, self._y0)).draw(self._win.canvas, cell_color)
        if self.has_right_wall:
            Line(Point(self._x1, self._y1), Point(self._x1, self._y0)).draw(self._win.canvas, cell_color)
        if self.has_bottom_wall:
            Line(Point(self._x0, self._y1), Point(self._x1, self._y1)).draw(self._win.canvas, cell_color)

    def draw_move(self, to_cell, undo=False):
        from_point = Point((self._x0 + self._x1)/2, (self._y0 + self._y1)/2)
        to_point = Point((to_cell._x0 + to_cell._x1)/2, (to_cell._y0 + to_cell._y1)/2)
        Line(from_point, to_point).draw(self._win.canvas, "red" if undo else "gray")
