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
        self.__top_wall_exists = True
        self.__bottom_wall_exists = True
        self.__left_wall_exists = True
        self.__right_wall_exists = True
        self.__top_wall = Line(Point(x1, y1), Point(x2, y1))
        self.__bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        self.__left_wall = Line(Point(x1, y1), Point(x1, y2))
        self.__right_wall = Line(Point(x2, y1), Point(x2, y2))
        self.__window = window

    def set_walls(self, top: bool, bottom: bool, left: bool, right: bool):
        self.__top_wall_exists = top
        self.__bottom_wall_exists = bottom
        self.__left_wall_exists = left
        self.__right_wall_exists = right

    def draw(self):
        if self.__top_wall_exists:
            self.__window.draw_line(self.__top_wall)
        if self.__bottom_wall_exists:
            self.__window.draw_line(self.__bottom_wall)
        if self.__left_wall_exists:
            self.__window.draw_line(self.__left_wall)
        if self.__right_wall_exists:
            self.__window.draw_line(self.__right_wall)
