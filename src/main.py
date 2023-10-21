import sys

import click

from .puzzle.reader import SudokuReader
from .puzzle.saver import SudokuSaver
from .puzzle.sudoku import Difficulty, Sudoku
from .types.sudoku_types import GenerationOutput
from .types.validation import (
    difficulty_choices,
    generation_output_choices,
    validate_generation_output,
    validate_sudoku_difficulty,
)


@click.group(help="Sudoku Puzzle Generator and Solver")
def main() -> None:
    """
    A command-line utility to generate and solve Sudoku puzzles.
    """
    pass


@main.command()
@click.option(
    "-d",
    "--difficulty",
    type=click.Choice(difficulty_choices, case_sensitive=False),
    callback=validate_sudoku_difficulty,
    default=Difficulty.EASY.name.lower(),
    show_default=True,
    show_choices=True,
    help=f"Generate a Sudoku puzzle with the specified difficulty level. Choose from: extreme_easy, easy, medium, difficult, hellish.",
)
@click.option(
    "-o",
    "--output",
    type=click.Choice(generation_output_choices, case_sensitive=False),
    callback=validate_generation_output,
    default=GenerationOutput.STDOUT.lower(),
    show_default=True,
    show_choices=True,
    help=f"Specify the output destination for the generated Sudoku puzzle. Choose from: {', '.join(generation_output_choices)}.",
)
def generate(difficulty: Difficulty, output: str) -> None:
    sudoku = Sudoku()
    sudoku.generate_puzzle(difficulty=difficulty)
    sudoku_saver = SudokuSaver(sudoku)
    if output == GenerationOutput.STDOUT:
        sudoku.print_puzzle(title=f"{difficulty.name.capitalize()} difficulty")
    elif output == GenerationOutput.FILE:
        sudoku_saver.save_puzzle_as_image()
    elif output == GenerationOutput.IMAGE:
        sudoku_saver.save_puzzle_as_image()
    else:
        raise ValueError(f"Invalid output: {output}")


@main.command()
@click.option(
    "-f",
    "--file",
    type=click.Path(exists=True),
    help="The path to the Sudoku puzzle file.",
    required=True,
)
def solve(file: str) -> None:
    try:
        sudoku: Sudoku = SudokuReader.read_puzzle(file)
        sudoku.solve()
        sudoku.print_puzzle(title="Solved Sudoku")
    except ValueError as e:
        error_message = str(e).strip()
        sys.stderr.write(error_message + "\n")


if __name__ == "__main__":
    main()
