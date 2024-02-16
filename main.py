from graphics import Window
from maze import Maze
from solver import Solver


def main():
    window = Window(800, 800)

    game = Maze(
        x_position=10,
        y_position=10,
        height=16,
        width=16,
        cell_height=40,
        cell_width=40,
        window=window
    )

    solver = Solver(game)

    if solver.solve():
        print("Maze solved successfully :)")
    else:
        print("I'm unable to solve the maze :(")

    window.mainloop()


if __name__ == "__main__":
    main()
