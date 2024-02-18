from typing import List
import random
from enum import Enum
from graphics import Graphics
from cell import Cell, CellWallLabels


class MazeDirection(Enum):
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

    def __init__(self, i: int, j: int, last_i: int, last_j: int):
        self.i = i
        self.j = j
        self.last_i = last_i
        self.last_j = last_j

    def __eq__(self, other) -> bool:
        if (self.i == other.i) and (self.j == other.j) and (self.last_i == other.last_i) and (self.last_j == other.last_j):
            return True
        return False

    def get_adjacent_position(
            self,
            direction: MazeDirection
    ) -> 'MazePosition':
        """
        calculate and return the position on the maze that is directly adjacent
        to this maze position in the specified direction. If the adjacent
        position is outside the boundaries of the maze then a value of None
        is returned.
        """
        if direction not in MazeDirection:
            raise TypeError(
                "The argument does not appear to be a valid maze direction."
            )

        if direction is MazeDirection.ABOVE and (self.i-1 >= 0):
            return MazePosition(
                i=self.i-1,
                j=self.j,
                last_i=self.last_i,
                last_j=self.last_j,
            )
        if direction is MazeDirection.BELOW and (self.i+1 <= self.last_i):
            return MazePosition(
                i=self.i+1,
                j=self.j,
                last_i=self.last_i,
                last_j=self.last_j,
            )
        if direction is MazeDirection.LEFT and (self.j-1 >= 0):
            return MazePosition(
                i=self.i,
                j=self.j-1,
                last_i=self.last_i,
                last_j=self.last_j,
            )
        if direction is MazeDirection.RIGHT and (self.j+1 <= self.last_j):
            return MazePosition(
                i=self.i,
                j=self.j+1,
                last_i=self.last_i,
                last_j=self.last_j,
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
            height: int,
            width: int,
            cell_height: int,
            cell_width: int,
            graphics: Graphics = None,
            seed=None,
    ) -> None:
        self._x_position = x_position
        self._y_position = y_position
        self._height = height
        self._width = width
        self._cell_height = cell_height
        self._cell_width = cell_width
        self._graphics = graphics
        self._generator = "generator"

        # initialise the random number generator
        random.seed(seed)

        # Create the Maze's cells
        self._cell_grid: List[List[Cell]] = None

    def generate(self):
        """
        randomly generates a new maze.
        """

        if self._cell_grid is None:
            self._cell_grid: List[List[Cell]] = None
            self._create_cell_grid()
        else:
            self._graphics.clear_all()
            self._reset_cell_grid()

        if self._graphics:
            self._draw_cell_grid()

        self._open_entrance_and_exit()
        self._break_walls_r(MazePosition(
            i=0,
            j=0,
            last_i=self._height-1,
            last_j=self._width-1,
        ))

    def get_last_i(self) -> int:
        "returns the last position of the Maze's outer list."

        return self._height-1

    def get_last_j(self) -> int:
        "returns the last position of the Maze's inner list."

        return self._width-1

    def _create_cell_grid(self) -> None:
        """
        creates all the cells and draws them.
        """

        self._cell_grid: List[List[Cell]] = [None for i in range(self._height)]
        cursor_x = self._x_position
        cursor_y = self._y_position

        for i in range(self._height):
            cells: List[Cell] = [None for j in range(self._width)]
            for j in range(self._width):
                cell = Cell(
                    cursor_x,
                    cursor_y,
                    (cursor_x + self._cell_width),
                    (cursor_y + self._cell_height),
                )
                cells[j] = cell
                if j == self._width - 1:
                    cursor_x = self._x_position
                else:
                    cursor_x += self._cell_width
            self._cell_grid[i] = cells
            cursor_y += self._cell_height

    def _draw_cell_grid(self) -> None:
        """
        draws all the cells on the maze with a short pause between each cell
        for animation purposes.
        """

        for i in range(self._height):
            for j in range(self._width):
                self._draw_cell(i=i, j=j)

    def _open_entrance_and_exit(self) -> None:
        """
        opens the maze's entrance and exit cells by breaking their respective
        walls. The entrance is located at the top left and the exit is located
        at the bottom right of the maze.
        """

        self._cell_grid[0][0].configure_walls(top=False)
        self._cell_grid[self._height-1][self._width -
                                        1].configure_walls(bottom=False)

        if self._graphics:
            self._draw_cell(0, 0)
            self._draw_cell(
                i=self._height-1,
                j=self._width-1
            )

    def _break_walls_r(self, current_position: MazePosition) -> None:
        """
        _break_walls_r generates a random maze by traversing through the
        cells and randomly knocking down the walls to create the maze's paths.
        """

        self.mark_cell_as_visited(
            i=current_position.i,
            j=current_position.j,
            visitor=self._generator,
        )

        while True:
            possible_directions: List[MazeDirection] = []

            for direction in MazeDirection:
                adjacent_position = current_position.get_adjacent_position(
                    direction)
                if adjacent_position is None:
                    continue
                if self.cell_was_visited_by(
                        i=adjacent_position.i,
                        j=adjacent_position.j,
                        visitor=self._generator,
                ):
                    continue
                possible_directions.append(direction)

            if len(possible_directions) == 0:
                if self._graphics:
                    self._draw_cell(i=current_position.i, j=current_position.j)
                break

            chosen_direction = random.choice(possible_directions)
            next_position = current_position.get_adjacent_position(
                chosen_direction)

            if chosen_direction is MazeDirection.ABOVE:
                self._configure_cell_walls(
                    i=current_position.i,
                    j=current_position.j,
                    top=False,
                )
                self._configure_cell_walls(
                    i=next_position.i,
                    j=next_position.j,
                    bottom=False,
                )
            elif chosen_direction is MazeDirection.BELOW:
                self._configure_cell_walls(
                    i=current_position.i,
                    j=current_position.j,
                    bottom=False,
                )
                self._configure_cell_walls(
                    i=next_position.i,
                    j=next_position.j,
                    top=False,
                )
            elif chosen_direction is MazeDirection.LEFT:
                self._configure_cell_walls(
                    i=current_position.i,
                    j=current_position.j,
                    left=False,
                )
                self._configure_cell_walls(
                    i=next_position.i,
                    j=next_position.j,
                    right=False,
                )
            elif chosen_direction is MazeDirection.RIGHT:
                self._configure_cell_walls(
                    i=current_position.i,
                    j=current_position.j,
                    right=False,
                )
                self._configure_cell_walls(
                    i=next_position.i,
                    j=next_position.j,
                    left=False,
                )

            if self._graphics:
                self._draw_cell(i=current_position.i, j=current_position.j)

            self._break_walls_r(next_position)

    def _draw_cell(self, i: int, j: int) -> None:
        """
        draws the cells in an animated way.
        """

        self._graphics.draw_cell_walls(self._cell_grid[i][j].get_walls())

    def _draw_path(self, current_cell: Cell, next_cell: Cell, undo: bool = False) -> None:
        """
        draws a path between two cells in an animated way.
        """

        self._graphics.draw_path(
            current_cell.centre(), next_cell.centre(), undo)

    def mark_cell_as_visited(self, i: int, j: int, visitor: str) -> None:
        """
        marks the cell at the specified position by the specified visitor.
        """

        self._cell_grid[i][j].mark_as_visited_by(visitor)

    def cell_was_visited_by(self, i: int, j: int, visitor: str) -> bool:
        """
        returns True if the cell at the specified position was visited by
        the specified visitor.
        """

        return self._cell_grid[i][j].was_visited_by(visitor)

    def cell_wall_exists(self, i: int, j: int, wall: CellWallLabels) -> bool:
        """
        returns true if a specified cell's wall exists.
        """

        return self._cell_grid[i][j].wall_exists(wall)

    def draw_path_between(self, a: MazePosition, b: MazePosition, undo: bool = False) -> None:
        """
        draws a path between position A and position B
        """

        cell_a = self._cell_grid[a.i][a.j]
        cell_b = self._cell_grid[b.i][b.j]

        self._draw_path(cell_a, cell_b, undo)

    def _configure_cell_walls(
        self,
        i: int,
        j: int,
        top: bool = None,
        bottom: bool = None,
        left: bool = None,
        right: bool = None,
    ) -> None:
        """
        (re)configures the walls of the specified cell.
        """

        self._cell_grid[i][j].configure_walls(
            top=top,
            bottom=bottom,
            left=left,
            right=right,
        )

    def _reset_cell_grid(self) -> None:
        for i in range(self._height):
            for j in range(self._width):
                self._cell_grid[i][j].reset()

    def reset_solution(self, visitor: str) -> None:
        self._graphics.clear_paths()
        for i in range(self._height):
            for j in range(self._width):
                self._cell_grid[i][j].unmark_visited(visitor)
