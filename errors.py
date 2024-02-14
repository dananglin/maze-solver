class CellInvalidError(Exception):
    """
    CellInvalidError is raised when the program tries to create a Cell whose
    values are invalid. The values are invalid when x2 is smaller than x1
    and/or y2 is smaller than y1. When creating a Cell the x and y values
    should always represent the top left and the bottom right corners of
    the cell (i.e. x1 < x2 and y1 < y2).
    """

    def __init__(self, x1: int, y1: int, x2: int, y2: int, *args):
        super().__init__(args)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __str__(self):
        return f"Invalid Cell values received. Please ensure that both: x1 ({self.x1}) < x2 ({self.x2}), and y1 ({self.y1}) < y2 ({self.y2})"


class CellTooSmallError(Exception):
    """
    CellTooSmallError is raised when the program tries to create a Cell
    which is too small to correctly draw it's central point.
    """

    def __init__(self, size_type: str, size: int, *args):
        super().__init__(args)
        self.size_type = size_type
        self.size = size

    def __str__(self):
        return f"The {self.size_type} size of the cell ({self.size}) is too small."
