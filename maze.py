from typing import List
from time import sleep
import random
from enum import Enum
from graphics import Window
from cell import Cell


class MazeDirections(Enum):
    """
    MazeDirection represents the directions you can
    take in the maze.
    """
    ABOVE = 0
    BELOW = 1
    LEFT = 2
    RIGHT = 3


class MazePosition:
    """
    MazePosition represents a position on the maze grid.
    """

    def __init__(self, i: int, j: int, max_i: int, max_j: int):
        self.i = i
        self.j = j
        self.max_i = max_i
        self.max_j = max_j

    def __eq__(self, other) -> bool:
        if (self.i == other.i) and (self.j == other.j) and (self.max_i == other.max_i) and (self.max_j == other.max_j):
            return True
        return False

    def get_adjacent_position(
            self,
            direction: MazeDirections
    ) -> 'MazePosition':
        if direction not in MazeDirections:
            raise TypeError(
                "The argument does not appear to be a valid MazeDirection"
            )

        if direction is MazeDirections.ABOVE and (self.i-1 >= 0):
            return MazePosition(
                i=self.i-1,
                j=self.j,
                max_i=self.max_i,
                max_j=self.max_j,
            )
        if direction is MazeDirections.BELOW and (self.i+1 <= self.max_i):
            return MazePosition(
                i=self.i+1,
                j=self.j,
                max_i=self.max_i,
                max_j=self.max_j,
            )
        if direction is MazeDirections.LEFT and (self.j-1 >= 0):
            return MazePosition(
                i=self.i,
                j=self.j-1,
                max_i=self.max_i,
                max_j=self.max_j,
            )
        if direction is MazeDirections.RIGHT and (self.j+1 <= self.max_j):
            return MazePosition(
                i=self.i,
                j=self.j+1,
                max_i=self.max_i,
                max_j=self.max_j,
            )

        return None


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
        self._cells: List[List[Cell]] = [
            None for i in range(self._num_cell_rows)]
        self._create_cell_grid()
        self._open_entrance_and_exit()

        start_position = MazePosition(
            i=0,
            j=0,
            max_i=self._num_cell_rows-1,
            max_j=self._num_cells_per_row-1,
        )

        end_position = MazePosition(
            i=self._num_cell_rows-1,
            j=self._num_cells_per_row-1,
            max_i=self._num_cell_rows-1,
            max_j=self._num_cells_per_row-1,
        )

        self._break_walls_r(start_position)

    def _create_cell_grid(self) -> None:
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
            self._draw_cell_grid()

    def _draw_cell_grid(self) -> None:
        """
        draws all the cells on the maze with a short pause between each cell
        for animation purposes.
        """
        for i in range(self._num_cell_rows):
            for j in range(self._num_cells_per_row):
                self._draw_cell(i=i, j=j)

    def _open_entrance_and_exit(self) -> None:
        """
        opens the maze's entrance and exit cells by breaking their respective
        walls. The entrance is located at the top left and the exit is located
        at the bottom right of the maze.
        """
        self._cells[0][0].configure_walls(top=False)
        self._cells[self._num_cell_rows -
                    1][self._num_cells_per_row-1].configure_walls(bottom=False)

        if self._window:
            self._draw_cell(0, 0)
            self._draw_cell(
                i=self._num_cell_rows-1,
                j=self._num_cells_per_row-1
            )

    def _break_walls_r(self, current_position: MazePosition) -> None:
        """
        _break_walls_r generates a random maze by traversing through the
        cells and randomly knocking down the walls to create the maze's paths.
        """

        current_cell = self._cells[current_position.i][current_position.j]
        current_cell.visited_by_maze_generator = True

        while True:
            possible_directions: List[MazeDirections] = []

            for direction in MazeDirections:
                adjacent_position = current_position.get_adjacent_position(
                    direction)
                if adjacent_position is None:
                    continue
                adjacent_cell = self._cells[adjacent_position.i][adjacent_position.j]
                if adjacent_cell.visited_by_maze_generator:
                    continue
                possible_directions.append(direction)

            if len(possible_directions) == 0:
                if self._window:
                    self._draw_cell(i=current_position.i, j=current_position.j)
                break

            chosen_direction = random.choice(possible_directions)
            next_position = current_position.get_adjacent_position(
                chosen_direction)
            next_cell = self._cells[next_position.i][next_position.j]

            if chosen_direction is MazeDirections.ABOVE:
                current_cell.configure_walls(top=False)
                next_cell.configure_walls(bottom=False)
            elif chosen_direction is MazeDirections.BELOW:
                current_cell.configure_walls(bottom=False)
                next_cell.configure_walls(top=False)
            elif chosen_direction is MazeDirections.LEFT:
                current_cell.configure_walls(left=False)
                next_cell.configure_walls(right=False)
            elif chosen_direction is MazeDirections.RIGHT:
                current_cell.configure_walls(right=False)
                next_cell.configure_walls(left=False)

            if self._window:
                self._draw_cell(i=current_position.i, j=current_position.j)

            self._break_walls_r(next_position)

    def _draw_cell(self, i: int, j: int) -> None:
        """
        _draw_cell draws the cells in an animated way.
        """
        self._cells[i][j].draw()
        self._window.redraw()
        sleep(0.05)
