from typing import Optional

import click

from .puzzle.sudoku import Difficulty, Sudoku

difficulty_choices: list[str] = [difficulty.name for difficulty in Difficulty]


def validate_sudoku_difficulty(
    _ctx: click.Context, _param: click.Parameter, value: Optional[str]
) -> Difficulty:
    """
    Validate the difficulty level of a Sudoku game.

    Args:
        _ctx (click.Context): The click context object.
        _param (click.Parameter): The click parameter object.
        value (Optional[str]): The value of the difficulty parameter.

    Returns:
        Difficulty: The validated difficulty level.

    Raises:
        click.BadParameter: If the difficulty level is invalid.
    """
    if value is None:
        return Difficulty.EASY

    try:
        return Difficulty[value]
    except ValueError:
        raise click.BadParameter(f"Invalid difficulty: {value}")


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
    default=Difficulty.EASY.name,
    show_default=True,
    show_choices=True,
    help=f"Generate a Sudoku puzzle with the specified difficulty level. Choose from: EXTREME_EASY, EASY, MEDIUM, DIFFICULT, HELLISH.",
)
def generate(difficulty: Difficulty) -> None:
    sudoku = Sudoku()
    sudoku.generate_puzzle(difficulty=difficulty)
    sudoku.print_puzzle(title=f"{difficulty.name.capitalize()} difficulty")


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
