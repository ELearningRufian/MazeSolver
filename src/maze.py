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
        self._cells = []
        for c in range(self.num_cols):
            current_col = []
            for r in range(self.num_rows):
                p0 = Point(self.x1 + c * self.cell_size_x, self.y1 + r * self.cell_size_y)
                p1 = Point(self.x1 + (c + 1) * self.cell_size_x, self.y1 + (r + 1) * self.cell_size_y)
                current_col.append(Cell(p0, p1, self.win))
            self._cells.append(current_col)
        [self._draw_cell(i, j) for i in range(self.num_cols) for j in range(self.num_rows)]

    def _draw_cell(self, i, j):
        self._cells[i][j].draw("black")
        self._animate()

    def _animate(self):
        self.win.redraw()
        sleep(0.05)