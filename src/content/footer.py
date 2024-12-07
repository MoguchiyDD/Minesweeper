# MIT License
#
# Copyright (c) 2024 MoguchiyDD
# URL: https://github.com/MoguchiyDD/Minesweeper


from tkinter import Tk, Frame, Button, font
from webbrowser import open

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

    def open_url() -> None:
        """
        Opens a URL with The OFFICIAL GitHub Page of The AUTHOR of
        The «МогучийДД (MoguchiyDD)» SOFTWARE
        """

        open("https://github.com/MoguchiyDD")

    copyright = Button(
        location,
        foreground=TEXT,
        background=DARK,
        activeforeground=TEXT,
        activebackground=DARK,
        highlightthickness=0,
        borderwidth=0,
        font=font.Font(size=FOOTER_FONT_SIZE),
        text=f"Copyright (c) 2024 MoguchiyDD",
        command=open_url
    )

    x_axis = (WIDTH - copyright.winfo_reqwidth()) // 2
    y_axis = (location_height - copyright.winfo_reqheight()) // 2
    copyright.place(x=x_axis, y=y_axis)

# --------------------------------
