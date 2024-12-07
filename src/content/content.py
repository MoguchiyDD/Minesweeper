# MIT License
#
# Copyright (c) 2024 MoguchiyDD
# URL: https://github.com/MoguchiyDD/Minesweeper


from tkinter import Tk, Frame, Label, font

from settings import (
    WIDTH,
    GRID_CELLS,
    HEADER_CELL_FONT_SIZE,
    PRIMARY,
    SECONDARY,
    HOVER,
    TEXT
)
from utils import frame_header, frame_content
from cell import Cell


# ------------ CONTENT ------------

def content(root: Tk, location_header: Frame) -> None:
    """
    Responsible for Drawing in The SOFTWARE CONTENT

    ---
    PARAMETERS:
    - root: Tk -> SOFTWARE WINDOW
    - location_header: Frame -> HEADER FRAME
    """

    header_height = frame_header()
    content_height = frame_content()

    content = Frame(
        root,
        background=PRIMARY,
        width=WIDTH,
        height=content_height
    )
    content.place(x=0, y=header_height)

    filling_content_data(root, content, location_header, header_height)


def filling_content_data(
    root: Tk,
    location_content: Frame,
    location_header: Frame,
    header_height: int,
    is_restart: bool = False
) -> None:
    """
    Filling The SOFTWARE CONTENT with DATA

    ---
    PARAMETERS:
    - root: Tk -> SOFTWARE WINDOW
    - location_content: Frame -> CONTENT FRAME
    - location_header: Frame -> HEADER FRAME
    - header_height: int -> HEADER HEIGHT FRAME
    - is_restart: bool -> Permission to RELOAD The HEADER and CONTENT
    of The SOFTWARE
    """

    def y_axis_label(label_width: int) -> int:
        """
        Calculates The Y-Axis to Place The LABEL

        ---
        PARAMETERS:
        - label_width: int -> Label WIDTH Issued from «Cell» CLASS
        ---
        RESULTS: Y-Axis
        """

        y_axis = (header_height - label_width) // 2
        return y_axis

    if is_restart:
        Cell.is_restart = True
        widgets_content = location_content.winfo_children()
        for x in range(GRID_CELLS):
            y = 0
            for widget in widgets_content:  # Update CELLS
                widget.configure(
                    foreground=SECONDARY,
                    background=SECONDARY,
                    activeforeground=HOVER,
                    activebackground=HOVER,
                    text=f"{ x }, { y }"
                )
                y += 1
    else:  # Create
        for x in range(GRID_CELLS):  # CELLS
            for y in range(GRID_CELLS):
                cell = Cell(x, y)
                cell.create_cell_btn(location_content)
                cell.cell_btn.grid(column=x, row=y)

        Cell.root = root
        Cell.link_filling_content_data = filling_content_data
        Cell.frame_content = location_content
        Cell.frame_header = location_header
        Cell.header_height = header_height

        # LABEL : CELLS
        Cell.create_cell_count_label(location_header)
        cell_y_axis = y_axis_label(Cell.cell_count_label.winfo_reqheight())
        Cell.cell_count_label.grid(column=0, row=0, pady=cell_y_axis)

        # LABEL : |
        vertical_line_label = Label(
            location_header,
            foreground=TEXT,
            background=PRIMARY,
            text=" | ",
            font=font.Font(size=HEADER_CELL_FONT_SIZE)
        )
        vl_y_axis = y_axis_label(Cell.cell_count_label.winfo_reqheight())
        vertical_line_label.grid(column=1, row=0, pady=vl_y_axis)

        # LABEL : BOMBS
        Cell.create_bomb_count_label(location_header)
        bomb_y_axis = y_axis_label(Cell.bomb_count_label.winfo_reqheight())
        Cell.bomb_count_label.grid(column=2, row=0, pady=bomb_y_axis)

    Cell.randomize_bomb()  # BOMBS
    Cell.is_restart = False

# ---------------------------------
