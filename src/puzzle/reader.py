from pathlib import Path

from ..puzzle.sudoku import Sudoku
from ..types.sudoku_types import Grid


class SudokuReader:
    @staticmethod
    def read_puzzle(filename: str) -> Sudoku:
        """
        Reads a Sudoku puzzle from a file.

        Parameters:
            filename (str): The name of the file containing the puzzle.

        Returns:
            Sudoku: A Sudoku object representing the puzzle.

        Raises:
            FileNotFoundError: If the file does not exist.
            NotImplementedError: If the file format is not supported.
        """
        file_path = Path(filename)

        if not file_path.is_file():
            raise FileNotFoundError(f"File '{filename}' does not exist.")

        if file_path.suffix == ".txt":
            puzzle: Grid = SudokuReader._read_txt_file(file_path)
        else:
            raise NotImplementedError("Unsupported file format.")

        sudoku = Sudoku()
        sudoku.set_puzzle(puzzle)
        return sudoku

    @staticmethod
    def _read_txt_file(file_path: Path) -> Grid:
        """
        Read a text file and convert its contents into a 2D grid.

        Args:
            file_path (Path): The path to the text file.

        Returns:
            Grid: A 2D grid representing the contents of the text file.
        """
        puzzle: Grid = []
        with open(file_path, "r") as f:
            for line in f:
                values: list[str] = line.replace(",", " ").replace("\n", "").split()
                row: list[int] = [
                    int(cell) if cell.isnumeric() else 0 for cell in values
                ]
                puzzle.append(row)

        return puzzle
