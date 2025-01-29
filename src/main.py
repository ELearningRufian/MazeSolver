from cell import *

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0,0), Point(800, 600)), "red")
    win.draw_line(Line(Point(800,0), Point(0, 600)), "red")
    cells = []
    cells.append(Cell(Point(80, 60), Point(720, 540), win))
    cells.append(Cell(Point(160, 120), Point(640, 480), win))
    cells.append(Cell(Point(240, 180), Point(560, 420), win))
    cells.append(Cell(Point(320, 240), Point(480, 360), win))
    cells[0].has_left_wall = False
    cells[1].has_top_wall = False
    cells[2].has_right_wall = False
    cells[3].has_bottom_wall = False
    for cell in cells:
        cell.draw("green")
    win.wait_for_close()

if __name__ == "__main__":
    main()