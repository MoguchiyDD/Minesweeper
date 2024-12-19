# MIT License
#
# Copyright (c) 2024 MoguchiyDD
# URL: https://github.com/MoguchiyDD/Minesweeper


from sys import platform


if platform == "win32":
    # TOTAL
    WIDTH = 522
    HEIGHT = 603

    # CELL
    WIDTH_CELL = 50
    HEIGHT_CELL = 50
    PAD_CELL = 2
else:
    # TOTAL
    WIDTH = 576
    HEIGHT = 603

    # CELL
    WIDTH_CELL = 36
    HEIGHT_CELL = 44
    PAD_CELL = 1


# TOTAL
TITLE = "Minesweeper Game"

# MODAL WINDOW
MW_WIDTH = WIDTH - 200
MW_BUTTON_WIDTH = MW_WIDTH // 19
MW_PADY = 10
MW_PADY_CONTENT = MW_PADY // 2
MW_GEOMETRY = MW_PADY ** 2

# NAMES
CELL_NAME = "Cells: "
BOMB_NAME = "Bombs: "
MW_LABEL_NAME_WIN = "You won. Start the game again?"
MW_LABEL_NAME_LOSE = "You lose. Start the game again?"
MW_YES_BUTTON_NAME = "Yes".upper()
MW_NO_BUTTON_NAME = "No".upper()

# CELLS
GRID_CELLS = 9
CELL_COUNT = GRID_CELLS ** 2
CELL_WIDTH_LABEL = WIDTH // 21
SIZE_CELLS = 13

# BOMBS
MIN_BOMB = 10
MAX_BOMB = 19
SIZE_BOMB = 19

# DIVS
HEADER_HEIGHT_DIV = 12
FOOTER_HEIGHT_DIV = 19

# FONTS
HEADER_CELL_FONT_SIZE = 13
FOOTER_FONT_SIZE = 9
MW_LABEL_FONT_SIZE = 11
MW_BUTTON_FONT_SIZE = 11

# COLORS
PRIMARY = "#0F172A"
SECONDARY = "#1E293B"
HOVER = "#334155"
DARK = "#020617"
TEXT = "#F1F5F9"
