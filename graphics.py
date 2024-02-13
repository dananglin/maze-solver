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

    def __init__(self, point_a: Point, point_b: Point) -> None:
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas: Canvas, fill_colour: str) -> None:
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

    def __init__(self, width: int, height: int) -> None:
        self._root = Tk()
        self._root.title("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)

        # Position the window to the centre of the screen
        screen_width = self._root.winfo_screenwidth()
        screen_height = self._root.winfo_screenheight()
        centre_x = int(screen_width/2 - width/2)
        centre_y = int(screen_height/2 - height/2)
        self._root.geometry(f"{width}x{height}+{centre_x}+{centre_y}")

        self._canvas = Canvas(self._root)
        self._canvas.config(
            bg="white",
            height=height,
            width=width,
        )
        self._canvas.pack()

        self._running = False

    def redraw(self) -> None:
        """
        redraw redraws all the graphics in the window.
        """
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self) -> None:
        """
        wait_for_close continuously redraws the window until
        it is set to close.
        """
        self._running = True
        while self._running:
            self.redraw()

    def draw_line(self, line: Line, fill_colour: str = "black") -> None:
        """
        draw_line draws a line on the canvas.
        """
        line.draw(self._canvas, fill_colour)

    def close(self) -> None:
        """
        close sets the window to close.
        """
        self._running = False
