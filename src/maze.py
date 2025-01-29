import random
from time import sleep
from cell import *

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        if 1 > num_rows:
            raise ValueError("The maze must have at least 1 row")
        if 1 > num_cols:
            raise ValueError("The maze must have at least 1 column")
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed is not None:
            random.seed(seed)
        self.cell_color = "black"
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        self._cells = [[Cell(self.win) for r in range(self.num_rows)] for c in range(self.num_cols)]
        [self._draw_cell(i, j) for j in range(self.num_rows) for i in range(self.num_cols)]

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        p0 = Point(self.x1 + i * self.cell_size_x, self.y1 + j * self.cell_size_y)
        p1 = Point(self.x1 + (i + 1) * self.cell_size_x, self.y1 + (j + 1) * self.cell_size_y)
        self._cells[i][j].draw(p0, p1, self.cell_color)
        self._animate()

    def _animate(self):
        self.win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[-1][-1]
        entrance_cell.has_top_wall = False
        exit_cell.has_bottom_wall = False
        entrance_cell.draw(None, None, self.cell_color)
        exit_cell.draw(None, None, self.cell_color)
    
    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            neighbors = []
            if 0 < i and not self._cells[i - 1][j].visited:
                neighbors.append({"col":i - 1, "row":j})
            if self.num_cols > i + 1 and not self._cells[i + 1][j].visited:
                neighbors.append({"col":i + 1, "row":j})
            if 0 < j and not self._cells[i][j - 1].visited:
                neighbors.append({"col":i, "row":j - 1})
            if self.num_rows > j + 1 and not self._cells[i][j + 1].visited:
                neighbors.append({"col":i, "row":j + 1})
            if 0 == len(neighbors):
                break
            neighbor = random.choice(neighbors)
            neighbor_cell = self._cells[neighbor["col"]][neighbor["row"]]
            if i > neighbor["col"]:
                current_cell.has_left_wall = False
                neighbor_cell.has_right_wall = False
            if i < neighbor["col"]:
                current_cell.has_right_wall = False
                neighbor_cell.has_left_wall = False
            if j > neighbor["row"]:
                current_cell.has_top_wall = False
                neighbor_cell.has_bottom_wall = False
            if j < neighbor["row"]:
                current_cell.has_bottom_wall = False
                neighbor_cell.has_top_wall = False
            self._draw_cell(i, j)
            self._draw_cell(neighbor["col"], neighbor["row"])
            self._break_walls_r(neighbor["col"], neighbor["row"])
