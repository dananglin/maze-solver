import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cell_grid(self):
        """
        test_maze_create_cell_grid tests that the maze is constructed properly.
        """
        cases = [
            {
                "number_of_cell_rows": 12,
                "number_of_cells_per_row": 10,
            },
            {
                "number_of_cell_rows": 50,
                "number_of_cells_per_row": 120,
            },
            {
                "number_of_cell_rows": 4,
                "number_of_cells_per_row": 4,
            },
        ]

        for case in cases:
            maze = Maze(
                0,
                0,
                case["number_of_cell_rows"],
                case["number_of_cells_per_row"],
                2,
                2,
            )
            self.assertEqual(
                len(maze._cells),
                case["number_of_cell_rows"],
            )
            self.assertEqual(
                len(maze._cells[0]),
                case["number_of_cells_per_row"],
            )

    def test_break_entrance_and_exit(self):
        """
        test_break_entrance_and_exit tests to ensure that the Maze's entry and
        exit Cells are open.
        """
        number_of_cell_rows = 5
        number_of_cells_per_row = 20
        maze = Maze(
            0,
            0,
            number_of_cell_rows,
            number_of_cells_per_row,
            2,
            2,
        )
        self.assertFalse(maze._cells[0][0]._top_wall.exists)
        self.assertFalse(
            maze._cells[number_of_cell_rows - 1][number_of_cells_per_row - 1]._bottom_wall.exists)


if __name__ == "__main__":
    unittest.main()
