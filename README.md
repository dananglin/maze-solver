# Maze Solver

## Overview

Maze Solver is an interactive maze simulator developed with Python and Tkinter.
With this application you can randomly generate mazes and watch as different algorithms try to solve them.

### Demo

![A demo of the Maze Solver application](assets/images/demo.gif)

### Repository mirrors

- **GitHub:** https://github.com/dananglin/maze-solver
- **Code Flow:** https://codeflow.dananglin.me.uk/apollo/maze-solver

## Requirements

To run the application you'll need a recent version of Python 3. This application was built and tested with Python 3.12.2.

You'll also need to make sure that you have `Tkinter` installed with your Python installation.
You can test this by running the following in your terminal:

```
python -m tkinter
```

If the module is installed then you should see a new small window appear on your screen.
If its not you'll see an error message starting with `ModuleNotFoundError` and you'll need to install it.
You may find guides online on how to install Tkinter for your operating system.

## How to run the application

Clone this repository to your local machine.

```
git clone https://github.com/dananglin/maze-solver.git
```

Run the application with Python.

```
cd maze-solver
python3 main.py
```

You should now see the Maze Solver window on your screen.

![Launching the application](assets/images/launch_application.png)

Generate a new maze by clicking on the `Generate maze` button and watch the application generate the maze.

Once the maze is generated choose which searching algorithm you want to see solve the maze.
As of writing `BFS` and `DFS` are available with more along the way.

Next choose if you want to enable randomness to the algorithm with the `Enable randomness` checkbox.
Randomness is applied when the solver stands before a fork in its path and has to choose from a number of possible directions.

With randomness enabled it will randomly choose the next direction and with it disabled the next direction is chosen
from something very similar to an ordered list.

![Selecting options](assets/images/option_selection.png)

Once you're happy with the options, click on the `Solve the maze` button to start the simulation.

As the solver traverses through the maze, it leaves a red trail so that you can keep track of its progress.

When the solver reaches a dead-end it backtracks until it can choose a new path to traverse.
When it backtracks it leaves behind a grey trail.

![Running the simulation](assets/images/running_the_simulation.png)

After the solver solves the maze (or fails to do so) you can run the simulation again on the same maze with by pressing the `Solve the maze` button.

Try running choosing a different algorithm or toggle between randomness before running the simulation again.

You can also generate a new maze by clicking the `Generate maze` button again.
