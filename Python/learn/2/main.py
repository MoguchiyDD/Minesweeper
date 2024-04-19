# Developer && Owner: МогучийДД (MoguchiyDD)
# LICENSE: MIT License which is located in the text file LICENSE
#
# Goal: Launch Working SOFTWARE
# Result: Opens The Finished SOFTWARE in The ACTIVE WINDOW
#
# Past Modification: Adding The «SOFTWARE» Block
# Last Modification: Editing The «SOFTWARE» Block (CELLS)
# Modification Date: 2024.04.19, 12:54 PM
#
# Create Date: 2024.04.18, 07:06 PM


from tkinter import Tk, Frame

from settings import (
    TITLE,
    WIDTH,
    HEIGHT,
    HEADER_HEIGHT_DIV,
    FOOTER_HEIGHT_DIV,
    GRID_CELLS,
    PRIMARY,
    DARK
)
from utils import height_div
from cell import Cell


# ------------ SOFTWARE ------------

root = Tk()

header_height = height_div(HEADER_HEIGHT_DIV)
footer_height = height_div(FOOTER_HEIGHT_DIV)
content_height = HEIGHT - header_height - footer_height

# Settings
root.configure(background=PRIMARY)

root.title(TITLE)
root.geometry(f"{ WIDTH }x{ HEIGHT }")  # set: WIDTHxHEIGHT
root.resizable(False, False)  # fixed: WIDTH, HEIGHT

# Content
header = Frame(
    root,
    background=PRIMARY,
    width=WIDTH,
    height=header_height
)
header.place(x=0, y=0)

content = Frame(
    root,
    background=PRIMARY,
    width=WIDTH,
    height=content_height
)
content.place(x=0, y=header_height)

footer = Frame(
    root,
    background=DARK,
    width=WIDTH,
    height=footer_height
)
footer.place(x=0, y=(content_height + header_height))

# CONTENT : Cells
for x in range(GRID_CELLS):
    for y in range(GRID_CELLS):
        cell = Cell(x, y)
        cell.create_cell_btn(content)
        cell.cell_btn.grid(column=x, row=y)

Cell.randomize_bomb()

# Run
root.mainloop()

# ----------------------------------
