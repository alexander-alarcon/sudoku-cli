from enum import Enum, StrEnum
from typing import NamedTuple

Grid = list[list[int]]


class DifficultyRange(NamedTuple):
    low_percentage: float
    high_percentage: float


class Difficulty(Enum):
    HELLISH = DifficultyRange(low_percentage=0.70, high_percentage=0.85)
    DIFFICULT = DifficultyRange(low_percentage=0.60, high_percentage=0.69)
    MEDIUM = DifficultyRange(low_percentage=0.45, high_percentage=0.59)
    EASY = DifficultyRange(low_percentage=0.35, high_percentage=0.44)
    EXTREME_EASY = DifficultyRange(low_percentage=0.21, high_percentage=0.26)


class GenerationOutput(StrEnum):
    FILE = "file"
    IMAGE = "image"
    STDOUT = "stdout"
