from graphics import Window
from cell import Cell


def main():
    window = Window(800, 800)

    cell_1 = Cell(10, 30, 100, 100, window)
    cell_1.configure_walls(top=True, bottom=True, left=True, right=False)
    cell_1.draw()

    cell_2 = Cell(210, 30, 300, 100, window)
    cell_2.configure_walls(top=True, bottom=False, left=False, right=True)
    cell_2.draw()

    cell_3 = Cell(210, 130, 300, 200, window)
    cell_3.configure_walls(top=False, bottom=True, left=True, right=True)
    cell_3.draw()

    cell_1.draw_move(cell_2)
    cell_2.draw_move(cell_3, undo=True)

    window.wait_for_close()


if __name__ == "__main__":
    main()
