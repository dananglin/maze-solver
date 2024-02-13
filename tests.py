import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cell_grid(self):
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
            maze = Maze(0, 0, case["number_of_cell_rows"], case["number_of_cells_per_row"], 2, 2)
            self.assertEqual(len(maze._cells), case["number_of_cell_rows"])
            self.assertEqual(len(maze._cells[0]), case["number_of_cells_per_row"])


if __name__ == "__main__":
    unittest.main()
