from graphics import Window
from maze import Maze


def main():
    window = Window(800, 800)

    _ = Maze(
        x_position=10,
        y_position=10,
        num_cell_rows=30,
        num_cells_per_row=30,
        cell_size_x=20,
        cell_size_y=20,
        window=window
    )

    window.mainloop()


if __name__ == "__main__":
    main()
