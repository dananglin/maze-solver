from typing import Dict
from enum import Enum
from line import Point, Line
import errors


class CellWallLabels(Enum):
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

    def __init__(self, line: Line) -> None:
        self._exists = True
        self._line = line
        self._line_colour = "black"

    def configure(self, build: bool) -> None:
        """
        builds or destroys the cell wall.
        """
        if build:
            self._build_wall()
        else:
            self._destroy_wall()

    def _build_wall(self) -> None:
        """
        builds the cell wall
        """
        self._exists = True
        self._line_colour = "black"

    def _destroy_wall(self) -> None:
        """
        destroys the cell wall
        """
        self._exists = False
        self._line_colour = "white"

    def wall_up(self) -> bool:
        """
        returns true if the cell wall is up.
        """
        return self._exists

    def get_line(self) -> Line:
        return self._line

    def get_line_colour(self) -> str:
        """
        returns the line colour of the wall.
        """
        return self._line_colour


class Cell:
    """
    A Cell represents a grid on the maze.
    """

    def __init__(
            self,
            x1: int, y1: int,
            x2: int, y2: int,
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

        self._walls: Dict[CellWallLabels, CellWall] = {
            CellWallLabels.TOP: CellWall(top_wall),
            CellWallLabels.BOTTOM: CellWall(bottom_wall),
            CellWallLabels.LEFT: CellWall(left_wall),
            CellWallLabels.RIGHT: CellWall(right_wall),
        }

        # Calculate the cell's central point
        centre_x = x1 + ((x2 - x1) / 2)
        centre_y = y1 + ((y2 - y1) / 2)
        self._centre = Point(centre_x, centre_y)

        self._visited: Dict[str, bool] = {
            "generator": False,
            "solver": False,
        }

    def configure_walls(
            self,
            top: bool = None,
            bottom: bool = None,
            left: bool = None,
            right: bool = None,
    ) -> None:
        """
        configure_walls configures the existence of the Cell's walls.
        """
        if top is not None:
            self._walls[CellWallLabels.TOP].configure(top)
        if bottom is not None:
            self._walls[CellWallLabels.BOTTOM].configure(bottom)
        if left is not None:
            self._walls[CellWallLabels.LEFT].configure(left)
        if right is not None:
            self._walls[CellWallLabels.RIGHT].configure(right)

    def centre(self) -> Point:
        """
        centre returns the Cell's central point
        """
        return self._centre

    def wall_exists(self, wall: CellWallLabels) -> bool:
        """
        returns True if a given cell wall exists, or false otherwise.
        """
        if wall not in CellWallLabels:
            raise TypeError(
                "The argument does not appear to be a valid cell wall."
            )
        return self._walls[wall].wall_up()

    def was_visited_by(self, visitor: str) -> bool:
        """
        returns True if the cell was visited by the
        specified visitor.
        """
        if visitor not in ("solver", "generator"):
            raise ValueError(f"This is an unknown visitor ({visitor})")

        return self._visited[visitor]

    def mark_as_visited_by(self, visitor: str) -> None:
        """
        marks the cell as visited by the specified visitor.
        """
        if visitor not in ("solver", "generator"):
            raise ValueError(f"This is an unknown visitor ({visitor})")
        self._visited[visitor] = True

    def unmark_visited(self, visitor: str) -> None:
        """
        unmarks the cell as visited by the specified visitor.
        """
        self._visited[visitor] = False

    def reset(self) -> None:
        for label in CellWallLabels:
            self._walls[label].configure(True)
        for k in self._visited:
            self._visited[k] = False

    def get_walls(self) -> Dict[CellWallLabels, CellWall]:
        return self._walls
