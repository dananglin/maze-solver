from typing import List
from time import sleep
from graphics import Window
from cell import Cell


class Maze:
    """
    Maze represents a two-dimensional grid of Cells.
    """

    def __init__(
            self,
            x_position: int,
            y_position: int,
            num_rows: int,
            num_columns: int,
            cell_size_x: int,
            cell_size_y: int,
            window: Window,
    ):
        self.__x_position = x_position
        self.__y_position = y_position
        self.__num_rows = num_rows
        self.__num_columns = num_columns
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window

        # Create the Maze's cells
        self.__cells: List[List[Cell]] = [None for i in range(self.__num_rows)]
        self.__create_cells()

    def __create_cells(self):
        cursor_x = self.__x_position
        cursor_y = self.__y_position

        for i in range(self.__num_rows):
            column: List[Cell] = [None for j in range(self.__num_columns)]
            for j in range(self.__num_columns):
                cell = Cell(
                    cursor_x,
                    cursor_y,
                    (cursor_x + self.__cell_size_x),
                    (cursor_y + self.__cell_size_y),
                    self.__window
                )
                column[j] = cell
                if j == self.__num_columns - 1:
                    cursor_x = self.__x_position
                else:
                    cursor_x += self.__cell_size_x
            self.__cells[i] = column
            cursor_y += self.__cell_size_y

        # Draw the maze in a dramatic way.
        self.__draw_cells()

    def __draw_cells(self):
        for i in range(self.__num_rows):
            for j in range(self.__num_columns):
                self.__cells[i][j].draw()
                self.__animate()

    def __animate(self):
        self.__window.redraw()
        sleep(0.05)
