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
