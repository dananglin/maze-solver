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
            num_cell_rows: int,
            num_cells_per_row: int,
            cell_size_x: int,
            cell_size_y: int,
            window: Window = None,
    ) -> None:
        self._x_position = x_position
        self._y_position = y_position
        self._num_cell_rows = num_cell_rows
        self._num_cells_per_row = num_cells_per_row
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window

        # Create the Maze's cells
        self._cells: List[List[Cell]] = [None for i in range(self._num_cell_rows)]
        self._create_cells()

    def _create_cells(self):
        cursor_x = self._x_position
        cursor_y = self._y_position

        for i in range(self._num_cell_rows):
            cells: List[Cell] = [None for j in range(self._num_cells_per_row)]
            for j in range(self._num_cells_per_row):
                cell = Cell(
                    cursor_x,
                    cursor_y,
                    (cursor_x + self._cell_size_x),
                    (cursor_y + self._cell_size_y),
                    self._window
                )
                cells[j] = cell
                if j == self._num_cells_per_row - 1:
                    cursor_x = self._x_position
                else:
                    cursor_x += self._cell_size_x
            self._cells[i] = cells
            cursor_y += self._cell_size_y

        if self._window:
            self._draw_cells()

    def _draw_cells(self):
        for i in range(self._num_cell_rows):
            for j in range(self._num_cells_per_row):
                self._cells[i][j].draw()
                self._animate()

    def _animate(self):
        self._window.redraw()
        sleep(0.05)
