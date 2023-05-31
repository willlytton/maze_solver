from cell import Cell
from graphics import Window
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        # creates a 2d array of cells
        self.cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self.create_cells()


    def create_cells(self):
        # iterates over the desired number of columns
        for i in range(self.num_cols):
            # for each column a new list is created to store the cells in that column
            col_cells = []
            # within column loop, iterate over the desired number of rows
            for j in range(self.num_rows):
                # for each row a new Cell instance is created and added to the col_cells list
                col_cells.append(Cell(self.win))
            # after the row loop is finished, the col_cells list, representing a column of cells[] is added to the cells list
            self.cells.append(col_cells)
        # Once the cells are created and added to cells[], the method proceeds to iterate over the column and rows to draw each cell
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cell(i, j)



    def draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.cells[i][j].draw(x1, y1, x2, y2)
        self.animate()

    
    def animate(self):
        if self.win is None:
            return
        Window.redraw()
        time.sleep(0.05)

    def break_entance_and_exit(self):
        # removes the left wall of the first cell
        self.cells[0][0].left = False
        self.draw_cell(0, 0)
        # removes the right wall of the last cell
        self.cells[self.num_cols - 1][self.num_rows - 1].right = False
        self.draw_cell(self.num_cols - 1, self.num_rows - 1)
