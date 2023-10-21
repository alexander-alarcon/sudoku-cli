import random
from typing import Optional

from prettytable import PrettyTable

from ..types.sudoku_types import Difficulty, Grid


class Sudoku:
    def __init__(self) -> None:
        """
        Initializes a new Sudoku grid with empty cells.

        The grid is represented as a 9x9 matrix, where each cell is initially set to 0.

        Returns:
            None
        """
        self.grid: Grid = [[0 for _ in range(9)] for _ in range(9)]

    def generate_puzzle(self, difficulty: Difficulty = Difficulty.MEDIUM) -> Grid:
        """
        Generate a new Sudoku puzzle.

        Returns:
            Grid: The generated Sudoku puzzle.
        """
        self.set_puzzle()
        self._remove_numbers(difficulty)
        return self.grid

    def solve(self) -> bool:
        """
        Solves the Sudoku puzzle recursively using backtracking.

        Returns:
            bool: True if the grid is filled successfully, False otherwise.
        """
        empty_cells: list[tuple[int, int]] = [
            (row, col)
            for row in range(9)
            for col in range(9)
            if self.grid[row][col] == 0
        ]

        if not empty_cells:
            return True  # The grid is filled successfully

        # Sort empty cells by the number of candidates
        empty_cells.sort(key=lambda cell: len(self._get_candidates(cell[0], cell[1])))

        row, col = empty_cells[0]
        candidates: list[int] = self._get_candidates(row, col)

        for num in candidates:
            self.grid[row][col] = num
            if self.solve():
                return True
            self.grid[row][col] = 0

        return False

    def set_puzzle(self, grid: Optional[Grid] = None) -> bool:
        """
        Sets the puzzle grid for the Sudoku object.

        Parameters:
            grid (Optional[Grid]): The grid representing the Sudoku puzzle. If not provided, a new empty grid will be used.

        Returns:
            bool: True if the puzzle grid was successfully set, False otherwise.
        """
        if grid:
            self.grid = grid
            return True

        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    candidates = list(range(1, 10))
                    random.shuffle(candidates)
                    for num in candidates:
                        if self._can_place(row, col, num):
                            self.grid[row][col] = num
                            if self.set_puzzle():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True

    def print_puzzle(self, title: Optional[str] = "Sudoku Puzzle") -> None:
        """
        Print the Sudoku puzzle.

        Args:
            title (Optional[str]): The title of the Sudoku puzzle. Defaults to "Sudoku Puzzle".

        Returns:
            None
        """
        table: PrettyTable = PrettyTable()

        table.title = title
        table.header = False
        for _, row in enumerate(self.grid):
            pretty_row: list[str] = [f"{num}" if num != 0 else " " for num in row]
            table.add_row(row=pretty_row, divider=True)  # type: ignore

        print(table)

    def _remove_numbers(self, difficulty: Difficulty) -> Grid:
        """
        Removes a specified number of cells from the grid based on the given difficulty.

        Parameters:
            difficulty (Difficulty): The difficulty level of the Sudoku puzzle.

        Returns:
            Grid: The modified grid with cells removed.
        """
        # Get all cell positions in the grid
        cell_positions: list[tuple[int, int]] = [
            (row, col) for row in range(9) for col in range(9)
        ]

        # Calculate the number of cells to remove based on difficulty
        lower_bound = int(difficulty.value.low_percentage * 81)  # 85% of 81
        upper_bound = int(difficulty.value.high_percentage * 81)  # 95% of 81
        num_cells_to_remove: int = random.randint(lower_bound, upper_bound)

        # Shuffle the list of cell positions
        random.shuffle(cell_positions)

        for i in range(num_cells_to_remove):
            row, col = cell_positions[i]
            self.grid[row][col] = 0

        return self.grid

    def _can_place(self, row: int, col: int, num: int) -> bool:
        """
        Check if a number can be placed in a specific position on the Sudoku board.

        Parameters:
            row (int): The row index of the position.
            col (int): The column index of the position.
            num (int): The number to be placed.

        Returns:
            bool: True if the number can be placed, False otherwise.
        """
        # Check the row
        if num in self._get_row_values(row):
            return False

        # Check the column
        if num in self._get_col_values(col):
            return False

        # Check the 3x3 box
        if num in self._get_block_values(row, col):
            return False

        return True

    def _get_candidates(self, row_values: int, col_values: int) -> list[int]:
        """
        Recursively fills the Sudoku grid with valid numbers.

        Parameters:
            row_values (int): The row index of the current cell.
            col_values (int): The column index of the current cell.

        Returns:
            list[int]: A list of valid numbers that can be placed in the current cell.
        """
        candidates = set(range(1, 10))
        candidates -= self._get_row_values(row_values)
        candidates -= self._get_col_values(col_values)
        candidates -= self._get_block_values(row_values, col_values)
        return list(candidates)

    def _get_row_values(self, row: int) -> set[int]:
        """
        Get the values in a specific row of the grid.

        Parameters:
            row (int): The index of the row to retrieve the values from.

        Returns:
            set[int]: A set containing the values in the specified row.
        """
        return set(self.grid[row])

    def _get_col_values(self, col: int) -> set[int]:
        """
        Get the values in a specific column of the grid.

        Parameters:
            col (int): The index of the column.

        Returns:
            set[int]: A set containing the values in the column.
        """

        return set(self.grid[row][col] for row in range(9))

    def _get_block_values(self, row: int, col: int) -> set[int]:
        """
        Get the values in the 3x3 block containing the given cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            set[int]: A set of values in the specified 3x3 block.
        """
        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        block_values: set[int] = set()

        for i in range(3):
            for j in range(3):
                block_values.add(self.grid[start_row + i][start_col + j])

        return block_values
