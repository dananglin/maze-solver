from graphics import Window
from maze import Maze
from solver import Solver


def main():
    window = Window(800, 800)

    game = Maze(
        x_position=10,
        y_position=10,
        height=19,
        width=19,
        cell_height=40,
        cell_width=40,
        window=window
    )

    solver = Solver(game)

    if solver.solve(solver.solve_with_randomised_dst_r):
        print("Maze solved successfully :)")
    else:
        print("I'm unable to solve the maze :(")

    window.mainloop()


if __name__ == "__main__":
    main()
