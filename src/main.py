import click

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
    if output == GenerationOutput.STDOUT:
        sudoku.print_puzzle(title=f"{difficulty.name.capitalize()} difficulty")
    else:
        sudoku.save_puzzle()


@main.command()
def solve() -> None:
    sudoku = Sudoku()
    sudoku.set_puzzle(
        grid=[
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
    )
    sudoku.solve()
    sudoku.print_puzzle(title="Solved")


if __name__ == "__main__":
    main()
