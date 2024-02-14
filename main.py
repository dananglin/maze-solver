from graphics import Window
from maze import Maze


def main():
    window = Window(800, 800)

    _ = Maze(10, 10, 30, 30, 20, 20, window)

    window.wait_for_close()


if __name__ == "__main__":
    main()
