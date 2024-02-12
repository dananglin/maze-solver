from tkinter import Tk, BOTH, Canvas


class Point:
    """
    Point represents the position of a point.
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    """
    Line represents a graphical line.
    """

    def __init__(self, point_a: Point, point_b: Point):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas: Canvas, fill_colour: str):
        """
        draw draws a line on a given canvas.
        """
        canvas.create_line(
            self.point_a.x, self.point_a.y,
            self.point_b.x, self.point_b.y,
            fill=fill_colour, width=2
        )
        canvas.pack()


class Window:
    """
    Window is a Graphical window.
    """

    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        # Position the window to the centre of the screen
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        centre_x = int(screen_width/2 - width/2)
        centre_y = int(screen_height/2 - height/2)
        self.__root.geometry(f"{width}x{height}+{centre_x}+{centre_y}")

        self.__canvas = Canvas(self.__root)
        self.__canvas.config(
            bg="white",
            height=height,
            width=width,
        )
        self.__canvas.pack()

        self.__is_running = False

    def redraw(self):
        """
        redraw redraws all the graphics in the window.
        """
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        """
        wait_for_close continuously redraws the window until
        it is set to close.
        """
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def draw_line(self, line: Line, fill_colour: str = "black"):
        """
        draw_line draws a line on the canvas.
        """
        line.draw(self.__canvas, fill_colour)

    def close(self):
        """
        close sets the window to close.
        """
        self.__is_running = False


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
