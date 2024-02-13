from graphics import Window, Point, Line


class Cell:
    """
    A Cell represents a grid on the maze.
    """

    def __init__(
            self,
            x1: int, y1: int,
            x2: int, y2: int,
            window: Window
    ):
        # Define the cell walls
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        left_wall = Line(Point(x1, y1), Point(x1, y2))
        right_wall = Line(Point(x2, y1), Point(x2, y2))

        self.__top_wall = CellWall(top_wall)
        self.__bottom_wall = CellWall(bottom_wall)
        self.__left_wall = CellWall(left_wall)
        self.__right_wall = CellWall(right_wall)

        # Calculate the cell's central point
        centre_x = x1 + ((x2 - x1) / 2)
        centre_y = y1 + ((y2 - y1) / 2)
        self.__centre = Point(centre_x, centre_y)

        # A reference to the root Window class for drawing purposes.
        self.__window = window

    def configure_walls(
            self,
            top: bool = True,
            bottom: bool = True,
            left: bool = True,
            right: bool = True,
    ):
        """
        configure_walls configures the existence of the Cell's walls.
        """
        self.__top_wall.exists = top
        self.__bottom_wall.exists = bottom
        self.__left_wall.exists = left
        self.__right_wall.exists = right

    def centre(self) -> Point:
        """
        centre returns the Cell's central point
        """
        return self.__centre

    def draw(self):
        """
        draw draws the cell onto the canvas
        """
        if self.__top_wall.exists:
            self.__window.draw_line(self.__top_wall.line)
        if self.__bottom_wall.exists:
            self.__window.draw_line(self.__bottom_wall.line)
        if self.__left_wall.exists:
            self.__window.draw_line(self.__left_wall.line)
        if self.__right_wall.exists:
            self.__window.draw_line(self.__right_wall.line)

    def draw_move(self, to_cell: 'Cell', undo: bool = False):
        """
        draw_move draws a path between the centre of this cell and
        the centre of the given cell.
        """
        fill_colour = "red"
        if undo:
            fill_colour = "grey"
        line = Line(self.centre(), to_cell.centre())
        self.__window.draw_line(line, fill_colour)


class CellWall:
    """
    A CellWall represents the existence (or non-existence) of
    a Cell's wall.
    """

    def __init__(self, line: Line):
        self.exists = True
        self.line = line
