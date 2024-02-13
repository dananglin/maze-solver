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
        self.__top_wall = CellWall(Line(Point(x1, y1), Point(x2, y1)))
        self.__bottom_wall = CellWall(Line(Point(x1, y2), Point(x2, y2)))
        self.__left_wall = CellWall(Line(Point(x1, y1), Point(x1, y2)))
        self.__right_wall = CellWall(Line(Point(x2, y1), Point(x2, y2)))
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


class CellWall:
    """
    A CellWall represents the existence (or non-existence) of
    a Cell's wall.
    """

    def __init__(self, line: Line):
        self.exists = True
        self.line = line
