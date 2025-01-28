from tkinter import Tk, BOTH, Canvas
from line import *

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("ELearningRufian's Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(height=height,width=width)
        self.canvas.pack()
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while True == self.running:
            self.redraw()
    
    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)