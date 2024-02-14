from typing import List
from time import sleep
import random
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
            seed=None,
    ) -> None:
        self._x_position = x_position
        self._y_position = y_position
        self._num_cell_rows = num_cell_rows
        self._num_cells_per_row = num_cells_per_row
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window

        # initialise the random number generator
        random.seed(seed)

        # Create the Maze's cells
        self._cells: List[List[Cell]] = [None for i in range(self._num_cell_rows)]
        self._create_cells()
        self._open_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self) -> None:
        """
        creates all the cells and draws them.
        """
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

    def _open_entrance_and_exit(self) -> None:
        """
        opens the maze's entrance and exit cells by breaking their respective
        walls. The entrance is located at the top left and the exit is located
        at the bottom right of the maze.
        """
        self._cells[0][0].configure_walls(top=False)
        self._cells[0][0].draw()

        self._cells[self._num_cell_rows-1][self._num_cells_per_row-1].configure_walls(bottom=False)
        self._cells[self._num_cell_rows-1][self._num_cells_per_row-1].draw()

    def _break_walls_r(self, y: int, x: int) -> None:
        current_cell = self._cells[y][x]
        current_cell.visited = True
        above, below, left, right = "above", "below", "left", "right"

        while True:
            adjacent_cells = {
                above: (y-1, x),
                below: (y+1, x),
                left: (y, x-1),
                right: (y, x+1),
            }
            to_visit: List[str] = []

            for k, value in adjacent_cells.items():
                if (value[0] < 0)or (value[1] < 0) or (value[0] > self._num_cell_rows-1) or (value[1] > self._num_cells_per_row-1):
                    continue
                if self._cells[value[0]][value[1]].visited:
                    continue

                to_visit.append(k)

            if len(to_visit) == 0:
                current_cell.draw()
                break

            next_direction = random.choice(to_visit)
            next_cell = self._cells[adjacent_cells[next_direction][0]][adjacent_cells[next_direction][1]]

            if next_direction is above:
                current_cell.configure_walls(top=False)
                next_cell.configure_walls(bottom=False)
            elif next_direction is below:
                current_cell.configure_walls(bottom=False)
                next_cell.configure_walls(top=False)
            elif next_direction is left:
                current_cell.configure_walls(left=False)
                next_cell.configure_walls(right=False)
            elif next_direction is right:
                current_cell.configure_walls(right=False)
                next_cell.configure_walls(left=False)

            current_cell.draw()
            next_cell.draw()
            self._animate()

            self._break_walls_r(
                adjacent_cells[next_direction][0],
                adjacent_cells[next_direction][1],
            )

    def _draw_cells(self) -> None:
        """
        draws all the cells on the maze with a short pause between each cell
        for animation purposes.
        """
        for i in range(self._num_cell_rows):
            for j in range(self._num_cells_per_row):
                self._cells[i][j].draw()
                self._animate()

    def _animate(self) -> None:
        """
        redraws the application and pauses for a short period of time to
        provide an animation effect.
        """
        self._window.redraw()
        sleep(0.05)
