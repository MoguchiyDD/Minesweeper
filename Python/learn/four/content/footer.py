# Developer && Owner: МогучийДД (MoguchiyDD)
# LICENSE: MIT License which is located in the text file LICENSE
#
# Goal: SOFTWARE FOOTER
# Result: Ready SOFTWARE FOOTER
#
# Past Modification: Adding COPYRIGHT
# Last Modification: Moving The FOOTER from «main.py» to «content/footer.py»
# Modification Date: 2024.04.20, 01:54 PM
#
# Create Date: 2024.04.20, 12:55 PM


from tkinter import Tk, Frame, Label, font

from settings import WIDTH, FOOTER_FONT_SIZE, DARK, TEXT
from utils import frame_header, frame_content, frame_footer


# ------------ FOOTER ------------

def footer(root: Tk) -> tuple[Frame, int]:
    """
    Responsible for Drawing in The SOFTWARE FOOTER

    ---
    PARAMETERS:
    - root: Tk -> SOFTWARE WINDOW
    ---
    RESULTS: (FOOTER, FOOTER HEIGHT)
    """

    footer_height = frame_footer()
    y_axis = frame_content() + frame_header()

    footer = Frame(
        root,
        background=DARK,
        width=WIDTH,
        height=footer_height
    )
    footer.place(x=0, y=y_axis)

    result = (footer, footer_height)
    return result


def footer_copyright(location: Frame, location_height: int) -> None:
    """
    COPYRIGHT Label for SOFTWARE FOOTER

    ---
    PARAMETERS:
    - location: Frame -> FOOTER for The LABEL
    - location_height: int -> FOOTER HEIGHT for The LABEL
    """

    copyright = Label(
        location,
        foreground=TEXT,
        background=DARK,
        text=f"Copyright (c) 2024 MoguchiyDD",
        font=font.Font(size=FOOTER_FONT_SIZE)
    )

    x_axis = (WIDTH - copyright.winfo_reqwidth()) // 2
    y_axis = (location_height - copyright.winfo_reqheight()) // 2
    copyright.place(x=x_axis, y=y_axis)

# --------------------------------
