from graphics import Window, Line, Point


def main():
    window = Window(800, 800)
    line_1 = Line(Point(10, 50), Point(100, 70))
    line_2 = Line(Point(300, 145), Point(456, 200))
    line_3 = Line(Point(20, 498), Point(50, 600))
    window.draw_line(line_1, "black")
    window.draw_line(line_2, "red")
    window.draw_line(line_3, "black")
    window.wait_for_close()


if __name__ == "__main__":
    main()
