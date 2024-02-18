import unittest
from cell import Cell, CellWallLabels
import maze
import errors


class Tests(unittest.TestCase):
    """
    Tests runs the test suite.
    """

    def test_maze_create_cell_grid(self):
        """
        test_maze_create_cell_grid tests that the maze is constructed properly.
        """
        cases = [
            {
                "height": 6,
                "width": 9,
            },
            {
                "height": 3,
                "width": 12,
            },
            {
                "height": 4,
                "width": 4,
            },
        ]

        for case in cases:
            m = maze.Maze(
                0,
                0,
                case["height"],
                case["width"],
                2,
                2,
                None,
                None,
            )
            self.assertEqual(
                len(m._cell_grid),
                case["height"],
            )
            self.assertEqual(
                len(m._cell_grid[0]),
                case["width"],
            )

    def test_break_entrance_and_exit(self):
        """
        test_break_entrance_and_exit tests to ensure that the Maze's entry and
        exit Cells are open.
        """
        number_of_cell_rows = 5
        number_of_cells_per_row = 20
        m = maze.Maze(
            0,
            0,
            number_of_cell_rows,
            number_of_cells_per_row,
            2,
            2,
            None,
            None,
        )
        m.generate()
        self.assertFalse(m._cell_grid[0][0].wall_exists(CellWallLabels.TOP))
        self.assertFalse(
            m._cell_grid[number_of_cell_rows - 1]
            [number_of_cells_per_row - 1].wall_exists(CellWallLabels.BOTTOM)
        )

    def test_invalid_cell_exception(self):
        """
        test_invalid_cell_exception tests the exception for when an attempt
        is made to create an invalid Cell.
        """
        cases = [
            {"x1": 30, "y1": 50, "x2": 20, "y2": 100},
            {"x1": 30, "y1": 50, "x2": 40, "y2": 25},
        ]

        for case in cases:
            with self.assertRaises(errors.CellInvalidError):
                _ = Cell(
                    x1=case["x1"],
                    y1=case["y1"],
                    x2=case["x2"],
                    y2=case["y2"]
                )

    def test_cell_too_small_exception(self):
        """
        test_cell_too_small_exception tests the exception for when an attempt
        is made to create a Cell that's too small.
        """
        cases = [
            {"x1": 1, "y1": 50, "x2": 2, "y2": 100},
            {"x1": 30, "y1": 25, "x2": 40, "y2": 25},
        ]

        for case in cases:
            with self.assertRaises(errors.CellTooSmallError):
                _ = Cell(
                    x1=case["x1"],
                    y1=case["y1"],
                    x2=case["x2"],
                    y2=case["y2"]
                )

    def test_maze_position_equality(self):
        cases = [
            {
                "m1": maze.MazePosition(i=1, j=3, last_i=10, last_j=100),
                "m2": maze.MazePosition(i=1, j=3, last_i=10, last_j=100),
                "expected": True,
            },
            {
                "m1": maze.MazePosition(i=1, j=3, last_i=10, last_j=100),
                "m2": maze.MazePosition(i=100, j=30, last_i=200, last_j=100),
                "expected": False,
            }
        ]

        for case in cases:
            result = case["m1"] == case["m2"]
            self.assertEqual(result, case["expected"])

    def test_maze_position_adjacent_positition(self):
        cases = [
            {
                "position": maze.MazePosition(i=3, j=4, last_i=10, last_j=10),
                "direction": maze.MazeDirection.ABOVE,
                "expected": maze.MazePosition(i=2, j=4, last_i=10, last_j=10),
            },
            {
                "position": maze.MazePosition(i=9, j=4, last_i=10, last_j=10),
                "direction": maze.MazeDirection.BELOW,
                "expected": maze.MazePosition(i=10, j=4, last_i=10, last_j=10),
            },
            {
                "position": maze.MazePosition(i=1, j=1, last_i=10, last_j=10),
                "direction": maze.MazeDirection.LEFT,
                "expected": maze.MazePosition(i=1, j=0, last_i=10, last_j=10),
            },
            {
                "position": maze.MazePosition(i=3, j=9, last_i=10, last_j=10),
                "direction": maze.MazeDirection.RIGHT,
                "expected": maze.MazePosition(i=3, j=10, last_i=10, last_j=10),
            },
            {
                "position": maze.MazePosition(i=0, j=4, last_i=10, last_j=10),
                "direction": maze.MazeDirection.ABOVE,
                "expected": None,
            },
            {
                "position": maze.MazePosition(i=10, j=4, last_i=10, last_j=10),
                "direction": maze.MazeDirection.BELOW,
                "expected": None,
            },
            {
                "position": maze.MazePosition(i=1, j=0, last_i=10, last_j=10),
                "direction": maze.MazeDirection.LEFT,
                "expected": None,
            },
            {
                "position": maze.MazePosition(i=3, j=10, last_i=10, last_j=10),
                "direction": maze.MazeDirection.RIGHT,
                "expected": None,
            },
        ]

        for case in cases:
            result = case["position"].get_adjacent_position(case["direction"])
            self.assertEqual(result, case["expected"])


if __name__ == "__main__":
    unittest.main()
