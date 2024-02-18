from typing import Dict, Tuple
from time import sleep
from tkinter import Canvas
from line import Line, Point
from cell import CellWallLabels, CellWall


class Graphics(Canvas):
    def __init__(self, container, background="white", width=800, height=800) -> None:
        super().__init__(container)
        self.config(
            bg=background,
            width=width,
            height=height,
        )
        self._path_tag = "path"
        self._cell_wall_tag = "cell_wall"

    def _redraw(self) -> None:
        """
        redraw redraws all the graphics in the window.
        """
        self.update_idletasks()
        self.update()
        sleep(0.05)

    def _draw_line(
            self,
            line: Line,
            tags: Tuple[str],
            fill_colour: str = "black",
            width: int = 2,
    ) -> None:
        """
        draws a line onto the canvas.
        """
        self.create_line(
            line.point_a.x, line.point_a.y,
            line.point_b.x, line.point_b.y,
            fill=fill_colour,
            width=width,
            tags=tags,
        )

    def draw_cell_walls(self, walls: Dict[CellWallLabels, CellWall]) -> None:
        """
        draws the walls of a cell onto the canvas.
        """
        for label in CellWallLabels:
            self._draw_line(
                line=walls[label].get_line(),
                fill_colour=walls[label].get_line_colour(),
                tags=(self._cell_wall_tag),
            )
        self._redraw()

    def draw_path(
            self,
            from_cell_centre: Point,
            to_cell_centre: Point,
            undo: bool = False
    ) -> None:
        """
        draws a path between the centre of this cell and
        the centre of the given cell.
        """
        line = Line(from_cell_centre, to_cell_centre)
        fill_colour = "red"
        if undo:
            fill_colour = "grey"
        self._draw_line(
            line=line,
            fill_colour=fill_colour,
            tags=(self._path_tag),
        )
        self._redraw()

    def clear_all(self) -> None:
        """
        clears the canvas
        """
        self.delete("all")

    def clear_paths(self) -> None:
        """
        deletes all the lines that have the
        path tag.
        """
        self.delete(self._path_tag)
