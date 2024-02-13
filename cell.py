from graphics import Window, Point, Line


class CellWall:
    """
    A CellWall represents the existence (or non-existence) of
    a Cell's wall.
    """

    def __init__(self, line: Line) -> None:
        self.exists = True
        self.line = line


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
        # Define the cell walls
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        left_wall = Line(Point(x1, y1), Point(x1, y2))
        right_wall = Line(Point(x2, y1), Point(x2, y2))

        self._top_wall = CellWall(top_wall)
        self._bottom_wall = CellWall(bottom_wall)
        self._left_wall = CellWall(left_wall)
        self._right_wall = CellWall(right_wall)

        # Calculate the cell's central point
        centre_x = x1 + ((x2 - x1) / 2)
        centre_y = y1 + ((y2 - y1) / 2)
        self._centre = Point(centre_x, centre_y)

        # A reference to the root Window class for drawing purposes.
        self._window = window

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
        self._top_wall.exists = top
        self._bottom_wall.exists = bottom
        self._left_wall.exists = left
        self._right_wall.exists = right

    def centre(self) -> Point:
        """
        centre returns the Cell's central point
        """
        return self._centre

    def draw(self) -> None:
        """
        draw draws the cell onto the canvas
        """
        if not self._window:
            return

        if self._top_wall.exists:
            self._window.draw_line(self._top_wall.line, fill_colour=self._window.cell_grid_colour)
        else:
            self._window.draw_line(self._top_wall.line, fill_colour=self._window.background_colour)

        if self._bottom_wall.exists:
            self._window.draw_line(self._bottom_wall.line, fill_colour=self._window.cell_grid_colour)
        else:
            self._window.draw_line(self._bottom_wall.line, fill_colour=self._window.background_colour)

        if self._left_wall.exists:
            self._window.draw_line(self._left_wall.line, fill_colour=self._window.cell_grid_colour)
        else:
            self._window.draw_line(self._left_wall.line, fill_colour=self._window.background_colour)

        if self._right_wall.exists:
            self._window.draw_line(self._right_wall.line, fill_colour=self._window.cell_grid_colour)
        else:
            self._window.draw_line(self._right_wall.line, fill_colour=self._window.background_colour)

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
