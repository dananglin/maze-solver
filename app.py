from tkinter import ttk, Tk, StringVar, BooleanVar
from maze import Maze
from solver import Solver
from graphics import Graphics


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Maze Solver")

        # Position the window to the centre of the screen
        height = 800
        width = 1000
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        centre_x = int(screen_width/2 - width/2)
        centre_y = int(screen_height/2 - height/2)
        self.geometry(f"{width}x{height}+{centre_x}+{centre_y}")
        self.resizable(False, False)

        # Styling
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.background_colour = "white"
        self.cell_grid_colour = "black"

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.graphics = Graphics(self)
        self.graphics.grid(column=1, row=0)

        self.maze = Maze(
            x_position=10,
            y_position=10,
            height=19,
            width=19,
            cell_height=40,
            cell_width=40,
            graphics=self.graphics,
        )

        self.solver = Solver(self.maze)

        self.search_algorithms = {
            "Breadth-First Search": self.solver.solve_with_dfs_r,
            "Depth-First Search": self.solver.solve_with_bfs_r,
        }

        self.side_panel = self._create_side_panel()
        self.side_panel.grid(column=0, row=0)

    def _create_side_panel(self):
        frame = ttk.Frame(self)
        label = ttk.Label(frame)
        label.config(text="Maze Solver", font=(None, 20))
        label.pack()
        generate = ttk.Button(
            frame,
            text="Generate maze",
            command=self.maze.generate,
        )
        generate.pack()
        tuple_of_algorithms = tuple(self.search_algorithms.keys())
        algorithm = StringVar()
        algorithm.set(tuple_of_algorithms[0])
        algorithm_label = ttk.Label(frame, text="Searching algorithm:")
        algorithm_label.pack()
        combobox = ttk.Combobox(frame, textvariable=algorithm)
        combobox["values"] = tuple_of_algorithms
        combobox["state"] = "readonly"
        combobox.pack()
        randomness = BooleanVar()
        enable_randomness = ttk.Checkbutton(frame)
        enable_randomness.config(
            text="Enable Randomness",
            variable=randomness,
            onvalue=True,
            offvalue=False,
        )
        enable_randomness.pack()
        solve = ttk.Button(
            frame,
            text="Solve the maze",
            command=lambda: self.solver.solve(
                solve_method=self.search_algorithms[algorithm.get()],
                enable_random_direction=randomness.get(),
            ),
        )
        solve.pack()
        return frame
