# Developer && Owner: МогучийДД (MoguchiyDD)
# LICENSE: MIT License which is located in the text file LICENSE
#
# Goal: Launch Working SOFTWARE
# Result: Opens The Finished SOFTWARE in The ACTIVE WINDOW
#
# Past Modification: Editing The «SOFTWARE» Block (CELLS && LABELS)
# Last Modification: Bug Fixed
# Modification Date: 2024.04.20, 02:37 PM
#
# Create Date: 2024.04.19, 07:24 PM


from tkinter import Tk, Label, font

from content.header import header
from content.content import content
from content.footer import footer, footer_copyright

from settings import (
    TITLE,
    WIDTH,
    HEIGHT,
    GRID_CELLS,
    HEADER_CELL_FONT_SIZE,
    PRIMARY,
    TEXT
)
from cell import Cell

from sys import path as syspath
syspath.append(__file__)


# ------------ SOFTWARE ------------

root = Tk()

# Settings
root.configure(background=PRIMARY)

root.title(TITLE)
root.geometry(f"{ WIDTH }x{ HEIGHT }")  # set: WIDTHxHEIGHT
root.resizable(False, False)  # fixed: WIDTH, HEIGHT

# Content : HEADER
func_header = header(root)
frame_header = func_header[0]
header_height = func_header[1]

# Content : CONTENT
frame_content = content(root)

for x in range(GRID_CELLS):  # Create CELLS
    for y in range(GRID_CELLS):
        cell = Cell(x, y)
        cell.create_cell_btn(frame_content)
        cell.cell_btn.grid(column=x, row=y)

# LABEL : CELLS
Cell.create_cell_count_label(frame_header)
cell_y_axis = (header_height - Cell.cell_count_label.winfo_reqheight()) // 2
Cell.cell_count_label.grid(column=0, row=0, pady=cell_y_axis)

# LABEL : |
vertical_line_label = Label(
    frame_header,
    foreground=TEXT,
    background=PRIMARY,
    text=" | ",
    font=font.Font(size=HEADER_CELL_FONT_SIZE)
)
vl_y_axis = (header_height - Cell.cell_count_label.winfo_reqheight()) // 2
vertical_line_label.grid(column=1, row=0, pady=vl_y_axis)

# LABEL : BOMBS
Cell.create_bomb_count_label(frame_header)
bomb_y_axis = (header_height - Cell.bomb_count_label.winfo_reqheight()) // 2
Cell.bomb_count_label.grid(column=2, row=0, pady=bomb_y_axis)

Cell.randomize_bomb()  # BOMBS

# Content : FOOTER
func_footer = footer(root)
frame_footer = func_footer[0]
footer_height = func_footer[1]
footer_copyright(frame_footer, footer_height)

# Run
root.mainloop()

# ----------------------------------
