from typing import Dict, Callable, List
import random
from maze import Maze, MazeDirection, MazePosition
from cell import CellWallLabels


class Solver:
    def __init__(self, game: Maze):
        self._game = game
        self._solver = "solver"

        # This is a dictionary mapping the direction to the maze to the
        # wall of the adjacent cell. It is used to identify the wall that could
        # potentially block the solver's path.
        # For example if the solver wants to move to the right, it's path
        # could be blocked by the adjacent cell's left wall.
        self._wall_map: Dict[MazeDirection, CellWallLabels] = {
            MazeDirection.ABOVE: CellWallLabels.BOTTOM,
            MazeDirection.BELOW: CellWallLabels.TOP,
            MazeDirection.LEFT: CellWallLabels.RIGHT,
            MazeDirection.RIGHT: CellWallLabels.LEFT,
        }

        random.seed()

    def _reset(self):
        self._game.reset_solution(self._solver)

    def solve(
        self,
        solve_method: Callable[[MazePosition, MazePosition, bool], bool],
        enable_random_direction: bool = False,
    ) -> bool:
        """
        solve attempts to solve the generated maze.
        """
        start_position = MazePosition(
            i=0,
            j=0,
            last_i=self._game.get_last_i(),
            last_j=self._game.get_last_j(),
        )

        end_position = MazePosition(
            i=self._game.get_last_i(),
            j=self._game.get_last_j(),
            last_i=self._game.get_last_i(),
            last_j=self._game.get_last_j(),
        )

        # Clear the maze if there was a previous run
        if self._game.cell_was_visited_by(
            i=start_position.i,
            j=start_position.j,
            visitor=self._solver,
        ):
            self._game.reset_solution(self._solver)

        return solve_method(
            start_position,
            end_position,
            enable_random_direction,
        )

    def solve_with_dfs_r(
            self,
            current_position: MazePosition,
            end_position: MazePosition,
            enable_random_direction: bool = False,
    ) -> bool:
        if current_position == end_position:
            return True

        self._game.mark_cell_as_visited(
            i=current_position.i,
            j=current_position.j,
            visitor=self._solver,
        )

        while True:
            possible_directions: List[MazeDirection] = []
            for direction in MazeDirection:
                adjacent_position = current_position.get_adjacent_position(
                    direction,
                )
                if adjacent_position is None:
                    continue
                if self._game.cell_was_visited_by(
                    i=adjacent_position.i,
                    j=adjacent_position.j,
                    visitor=self._solver,
                ) or self._game.cell_wall_exists(
                    i=adjacent_position.i,
                    j=adjacent_position.j,
                    wall=self._wall_map[direction],
                ):
                    continue
                possible_directions.append(direction)
            if len(possible_directions) == 0:
                break
            next_direction = None
            if len(possible_directions) == 1 or not enable_random_direction:
                next_direction = possible_directions[0]
            else:
                next_direction = random.choice(possible_directions)
            next_position = current_position.get_adjacent_position(
                next_direction,
            )
            self._game.draw_path_between(current_position, next_position)
            solved = self.solve_with_dfs_r(
                next_position, end_position)
            if solved:
                return True
            self._game.draw_path_between(
                current_position,
                next_position,
                undo=True
            )

        return False

    def solve_with_bfs_r(
        self,
        current_position: MazePosition,
        end_position: MazePosition,
        enable_random_direction: bool = False,
    ) -> bool:
        self._game.mark_cell_as_visited(
            i=current_position.i,
            j=current_position.j,
            visitor=self._solver,
        )

        while True:
            possible_directions = []
            for direction in MazeDirection:
                adjacent_position = current_position.get_adjacent_position(
                    direction,
                )

                if adjacent_position is None:
                    continue
                if self._game.cell_was_visited_by(
                        i=adjacent_position.i,
                        j=adjacent_position.j,
                        visitor=self._solver,
                ) or self._game.cell_wall_exists(
                    i=adjacent_position.i,
                    j=adjacent_position.j,
                    wall=self._wall_map[direction],
                ):
                    continue
                if adjacent_position == end_position:
                    self._game.draw_path_between(
                        current_position, adjacent_position)
                    return True

                possible_directions.append(direction)
            if len(possible_directions) == 0:
                break
            next_direction = None
            if len(possible_directions) == 1 or not enable_random_direction:
                next_direction = possible_directions[0]
            else:
                next_direction = random.choice(possible_directions)
            next_position = current_position.get_adjacent_position(
                next_direction,
            )
            self._game.draw_path_between(current_position, next_position)
            solved = self.solve_with_bfs_r(
                next_position,
                end_position,
                enable_random_direction
            )
            if solved:
                return True
            self._game.draw_path_between(
                current_position,
                next_position,
                undo=True
            )

        return False
