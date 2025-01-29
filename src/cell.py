from line import *
from window import *

class Cell:
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
        self._x0 = None
        self._y0 = None
        self._x1 = None
        self._y1 = None

    def draw(self, p0, p1, cell_color):
        if p0 is not None:
            self._x0 = p0.x
            self._y0 = p0.y
        if p1 is not None:
            self._x1 = p1.x
            self._y1 = p1.y
        if self._x0 is not None and self._y0 is not None and self._x1 is not None and self._y1 is not None:
            Line(Point(self._x0, self._y0), Point(self._x0, self._y1)).draw(self._win.canvas, cell_color if self.has_left_wall else "#d9d9d9")
            Line(Point(self._x1, self._y0), Point(self._x0, self._y0)).draw(self._win.canvas, cell_color if self.has_top_wall else "#d9d9d9")
            Line(Point(self._x1, self._y1), Point(self._x1, self._y0)).draw(self._win.canvas, cell_color if self.has_right_wall else "#d9d9d9")
            Line(Point(self._x0, self._y1), Point(self._x1, self._y1)).draw(self._win.canvas, cell_color if self.has_bottom_wall else "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        from_point = Point((self._x0 + self._x1)/2, (self._y0 + self._y1)/2)
        to_point = Point((to_cell._x0 + to_cell._x1)/2, (to_cell._y0 + to_cell._y1)/2)
        Line(from_point, to_point).draw(self._win.canvas, "red" if undo else "gray")
