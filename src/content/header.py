# MIT License
#
# Copyright (c) 2024 MoguchiyDD
# URL: https://github.com/MoguchiyDD/Minesweeper


from tkinter import Tk, Frame

from settings import WIDTH, PRIMARY
from utils import frame_header


# ------------ HEADER ------------

def header(root: Tk) -> tuple[Frame, int]:
    """
    Responsible for Drawing in The SOFTWARE HEADER

    ---
    PARAMETERS:
    - root: Tk -> SOFTWARE WINDOW
    ---
    RESULTS: (HEADER, HEADER HEIGHT)
    """

    header_height = frame_header()

    header = Frame(
        root,
        background=PRIMARY,
        width=WIDTH,
        height=header_height
    )
    header.place(x=0, y=0)

    result = (header, header_height)
    return result

# --------------------------------
