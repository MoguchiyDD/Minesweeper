# Developer && Owner: МогучийДД (MoguchiyDD)
# LICENSE: MIT License which is located in the text file LICENSE
#
# Goal: SOFTWARE HEADER
# Result: Ready SOFTWARE HEADER
#
# Past Modification: Adding COPYRIGHT
# Last Modification: Moving The HEADER from «main.py» to «content/header.py»
# Modification Date: 2024.04.20, 01:34 PM
#
# Create Date: 2024.04.20, 12:45 PM


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
