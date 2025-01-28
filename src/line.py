from point import *
class Line:
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1
        self.default_width = 2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p0.x, self.p0.y, self.p1.x, self.p1.y, fill=fill_color, width=self.default_width)