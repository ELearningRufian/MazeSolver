from time import sleep
from cell import *

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = [[Cell(self.win) for c in range(self.num_cols)] for r in range(self.num_rows)]
        [self._draw_cell(i, j) for i in range(self.num_rows) for j in range(self.num_cols)]

    def _draw_cell(self, i, j):
        p0 = Point(self.x1 + j * self.cell_size_x, self.y1 + i * self.cell_size_y)
        p1 = Point(self.x1 + (j + 1) * self.cell_size_x, self.y1 + (i + 1) * self.cell_size_y)
        self._cells[i][j].draw(p0, p1, "black")
        self._animate()

    def _animate(self):
        self.win.redraw()
        sleep(0.05)