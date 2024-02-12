from graphics import Window, Cell


def main():
    window = Window(800, 800)

    # Draw all walls
    cell_1 = Cell(10, 30, 100, 100, window)
    cell_1.draw()

    # Draw vertical walls only
    cell_2 = Cell(300, 50, 400, 100, window)
    cell_2.set_walls(False, False, True, True)
    cell_2.draw()

    # Draw horizontal walls only
    cell_3 = Cell(200, 400, 500, 600, window)
    cell_3.set_walls(True, True, False, False)
    cell_3.draw()

    window.wait_for_close()


if __name__ == "__main__":
    main()
