# Sudoku CLI

## Description

The Sudoku CLI is a command-line tool for generating and solving Sudoku puzzles. Sudoku is a classic number puzzle game that requires filling a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids contains all of the digits from 1 to 9. This project provides the functionality to generate Sudoku puzzles and solve them using the backtracking algorithm.

## Usage

### Generating Sudoku Puzzles

To generate a Sudoku puzzle, use the following command:

```shell
sudoku generate [OPTIONS]
```

Available options for generating puzzles:

-d, --difficulty: Set the difficulty of the puzzle. You can choose from [extreme_easy, easy, medium, hard, hellish]. The default difficulty is 'easy'.

-o, --output: Specify the output format of the puzzle. You can choose from 'stdout', 'file' or 'image'. The default output is 'stdout'. When using 'file' as the output format, a text file will be created in the current directory with the generated puzzle in space-separated values. Blank cells are represented with underscores ('_'). When using 'image' as the output format, a Sudoku puzzle image will be created in the current directory.

### Solving Sudoku Puzzles

To solve a Sudoku puzzle, use the following command:

```shell
sudoku solve [OPTIONS]
```

Available options for solving puzzles:

-f, --file: Set the input file containing the Sudoku puzzle to solve. The input file should contain comma or space-separated values representing the Sudoku grid. Blank spaces can be represented with any non-numeric character, except for commas or spaces.
