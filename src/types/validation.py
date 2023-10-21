from typing import Optional

import click

from ..types.sudoku_types import Difficulty, GenerationOutput

difficulty_choices: list[str] = [difficulty.name.lower() for difficulty in Difficulty]
generation_output_choices: list[str] = [
    generation_output.name.lower() for generation_output in GenerationOutput
]


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
        return Difficulty[value.upper()]
    except ValueError:
        raise click.BadParameter(f"Invalid difficulty: {value}")


def validate_generation_output(
    _ctx: click.Context, _param: click.Parameter, value: Optional[str]
) -> GenerationOutput:
    """
    Validate the generation output.

    Args:
        _ctx (click.Context): The click context.
        _param (click.Parameter): The click parameter.
        value (Optional[str]): The value to validate.

    Returns:
        GenerationOutput: The validated generation output.

    Raises:
        click.BadParameter: If the output is invalid.
    """
    if value is None:
        return GenerationOutput.STDOUT

    try:
        return GenerationOutput[value.upper()]
    except ValueError:
        raise click.BadParameter(f"Invalid output: {value}")
