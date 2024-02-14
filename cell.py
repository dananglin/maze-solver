from typing import Dict
from enum import Enum
from graphics import Window, Point, Line
import errors


class CellWallLabel(Enum):
    """
    CellWallLabel is used to label a CellWall
    """

    TOP = 0
    BOTTOM = 1
    LEFT = 2
    RIGHT = 3


class CellWall:
    """
    A CellWall represents the existence (or non-existence) of
    a Cell's wall.
    """

    def __init__(self, line: Line, window: Window) -> None:
        self.exists = True
        self.line = line
        self._window = window

    def draw(self):
        fill_colour = self._window.cell_grid_colour
        if not self.exists:
            fill_colour = self._window.background_colour

        self._window.draw_line(self.line, fill_colour=fill_colour)


class Cell:
    """
    A Cell represents a grid on the maze.
    """

    def __init__(
            self,
            x1: int, y1: int,
            x2: int, y2: int,
            window: Window = None,
    ) -> None:
        # Validation
        if (x2 < x1) or (y2 < y1):
            raise errors.CellInvalidError(x1, y1, x2, y2)

        if (x2 - x1) < 2:
            raise errors.CellTooSmallError("horizontal", x2-x1)

        if (y2 - y1) < 2:
            raise errors.CellTooSmallError("vertical", y2-y1)

        # Define the cell walls
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        left_wall = Line(Point(x1, y1), Point(x1, y2))
        right_wall = Line(Point(x2, y1), Point(x2, y2))

        self._walls: Dict[CellWallLabel, CellWall] = {
            CellWallLabel.TOP: CellWall(top_wall, window),
            CellWallLabel.BOTTOM: CellWall(bottom_wall, window),
            CellWallLabel.LEFT: CellWall(left_wall, window),
            CellWallLabel.RIGHT: CellWall(right_wall, window),
        }

        # Calculate the cell's central point
        centre_x = x1 + ((x2 - x1) / 2)
        centre_y = y1 + ((y2 - y1) / 2)
        self._centre = Point(centre_x, centre_y)

        # A reference to the root Window class for drawing purposes.
        self._window = window

        self.visited = False

    def configure_walls(
            self,
            top: bool = True,
            bottom: bool = True,
            left: bool = True,
            right: bool = True,
    ) -> None:
        """
        configure_walls configures the existence of the Cell's walls.
        """
        self._walls[CellWallLabel.TOP].exists = top
        self._walls[CellWallLabel.BOTTOM].exists = bottom
        self._walls[CellWallLabel.LEFT].exists = left
        self._walls[CellWallLabel.RIGHT].exists = right

    def centre(self) -> Point:
        """
        centre returns the Cell's central point
        """
        return self._centre

    def wall_exists(self, wall: CellWallLabel) -> bool:
        """
        returns True if a given cell wall exists, or false otherwise.
        """
        return self._walls[wall].exists

    def draw(self) -> None:
        """
        draw draws the cell onto the canvas
        """
        if not self._window:
            return

        for label in CellWallLabel:
            self._walls[label].draw()

    def draw_move(self, to_cell: 'Cell', undo: bool = False) -> None:
        """
        draw_move draws a path between the centre of this cell and
        the centre of the given cell.
        """
        if not self._window:
            return

        fill_colour = "red"
        if undo:
            fill_colour = "grey"
        line = Line(self.centre(), to_cell.centre())
        self._window.draw_line(line, fill_colour)
