from window import *

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(0,0),Point(800, 600)), "red")
    win.draw_line(Line(Point(800,0),Point(0, 600)), "red")
    win.wait_for_close()

if __name__ == "__main__":
    main()