from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont

from .sudoku import Sudoku


class SudokuSaver:
    def __init__(self, sudoku: Sudoku) -> None:
        """
        Initializes a new instance of the class.

        Args:
            sudoku (Sudoku): The Sudoku object that will be assigned to the 'sudoku' attribute.

        Returns:
            None
        """
        self.sudoku: Sudoku = sudoku

    def save_puzzle_as_txt(self, filename: str = "sudoku.txt") -> None:
        """
        Save the current puzzle grid to a file.

        Args:
            filename (str): The name of the file to save the puzzle to. Defaults to "sudoku.txt".

        Returns:
            None: This function does not return anything.
        """
        file_path = Path(filename)
        with open(file_path, "w") as f:
            for row in range(9):
                for col in range(8):
                    value: int = self.sudoku.grid[row][col]
                    f.write(f"{value if value != 0 else '_'} ")
                last_value: int = self.sudoku.grid[row][8]
                f.write(f"{last_value if last_value != 0 else '_'}\n")
        print(f"Saved puzzle to {file_path}")

    def save_puzzle_as_image(self, filename: str = "sudoku.png") -> None:
        """
        Save the Sudoku puzzle as an image file.

        Parameters:
            filename (str): The name of the file to save the image to. Defaults to "sudoku.png".

        Returns:
            None
        """
        # Define some constants for image creation
        cell_size: int = 100
        grid_size: int = cell_size * 9 + 20
        box_border_width: int = 5  # Width of the box boundaries
        image: Image.Image = Image.new("RGB", (grid_size, grid_size), "white")
        draw: ImageDraw.ImageDraw = ImageDraw.Draw(image)
        font: FreeTypeFont = ImageFont.truetype(
            font="/usr/share/fonts/TTF/CascadiaCode.ttf", size=70
        )

        # Draw the Sudoku grid
        for row in range(9):
            for col in range(9):
                cell_value: int = self.sudoku.grid[row][col]
                x1: float = col * cell_size
                y1: float = row * cell_size
                x2: float = x1 + cell_size
                y2: float = y1 + cell_size

                # Draw a rectangle for each cell
                draw.rectangle((x1, y1, x2, y2), outline="gray")

                # Draw the 3x3 box boundaries (thicker lines)
                if row % 3 == 0:
                    draw.line(
                        [(x1, y1), (x2, y1)], fill="black", width=box_border_width
                    )
                if col % 3 == 0:
                    draw.line(
                        [(x1, y1), (x1, y2)], fill="black", width=box_border_width
                    )

                if cell_value != 0:
                    draw.text(  # type: ignore
                        xy=(x1 + 30, y1 + 10),
                        text=str(cell_value),
                        fill="black",
                        font=font,
                    )

        # Save the image
        image.save(filename)
        print(f"Saved puzzle as image to {filename}")
