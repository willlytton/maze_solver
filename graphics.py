from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Game")
        self.canvas = Canvas(self.root, bg="white", width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()
        print("Window closed")

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = x

class Line:
    def __init__(self, P1, P2):
        self.P1 = P1
        self.P2 = P2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.P1.x, self.P1.y, self.P2.x, self.P2.y, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)
