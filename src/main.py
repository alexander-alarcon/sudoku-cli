from .puzzle.sudoku import Difficulty, Sudoku


def main() -> None:
    sudoku = Sudoku()
    sudoku.generate_puzzle(difficulty=Difficulty.HELLISH)
    sudoku.print_puzzle(title=f"{Difficulty.HELLISH.name.capitalize()} difficulty")


if __name__ == "__main__":
    main()
