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
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{self.width}x{self.height}")

        self.canvas = Canvas()
        self.canvas.pack()

        self.is_running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

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
        self.is_running = True
        while self.is_running:
            self.redraw()

    def draw_line(self, line: Line, fill_colour: str):
        """
        draw_line draws a line on the canvas.
        """
        line.draw(self.canvas, fill_colour)

    def close(self):
        """
        close sets the window to close.
        """
        self.is_running = False
