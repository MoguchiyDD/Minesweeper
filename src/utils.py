# MIT License
#
# Copyright (c) 2024 MoguchiyDD
# URL: https://github.com/MoguchiyDD/Minesweeper


from tkinter import Tk, Toplevel, Frame, Label, Button, font

from settings import (
    HEIGHT,
    MW_BUTTON_WIDTH,
    MW_PADY,
    MW_PADY_CONTENT,
    MW_GEOMETRY,
    MW_YES_BUTTON_NAME,
    MW_NO_BUTTON_NAME,
    HEADER_HEIGHT_DIV,
    FOOTER_HEIGHT_DIV,
    MW_LABEL_FONT_SIZE,
    MW_BUTTON_FONT_SIZE,
    PRIMARY,
    SECONDARY,
    HOVER,
    DARK,
    TEXT
)


# --------------- HEIGHT ---------------

def height_div(div: int) -> int:
    """
    Calculates The HEIGHT of a Block using a Divider

    ---
    PARAMETERS:
    - div: int -> Divider for HEIGHT Calculation
    ---
    RESULTS: HEIGHT ( e.g. 576) // divs (e.g. 12) => 48
    """

    result = HEIGHT // div
    return result

# --------------------------------------


# ------------ FRAME HEIGHT ------------

def frame_header() -> int:
    """
    HEADER HEIGHT for SOFTWARE

    ---
    RESULTS: HEADER HEIGHT
    """

    header_height = height_div(HEADER_HEIGHT_DIV)
    return header_height


def frame_content() -> int:
    """
    CONTENT HEIGHT for SOFTWARE

    ---
    RESULTS: CONTENT HEIGHT
    """

    content_height = HEIGHT - frame_header() - frame_footer()
    return content_height


def frame_footer() -> int:
    """
    FOOTER HEIGHT for SOFTWARE

    ---
    RESULTS: FOOTER HEIGHT
    """

    footer_height = height_div(FOOTER_HEIGHT_DIV)
    return footer_height

# --------------------------------------


# ------------ MODAL WINDOW ------------

def mw_win_or_lose(
    label_text: str,
    root: Tk,
    link_filling_content_data: object,
    location_content: Frame,
    location_header: Frame,
    header_height: int
):
    """
    MODAL WINDOW that Appears when The GAME IS OVER

    ---
    PARAMETERS:
    - label_text: str -> Text for MODAL WINDOW
    - root: Tk -> SOFTWARE WINDOW
    - link_filling_content_data: object -> Link to The «filling_content_data»
    FUNCTION from «content/content.py» FILE
    - location_content: Frame -> CONTENT FRAME
    - location_header: Frame -> HEADER FRAME
    - header_height: int -> HEADER HEIGHT FRAME
    """

    def restart() -> None:
        """
        Restarting The MINESWEEPER GAME
        """

        # CREATE : LABELS && CELLS
        mw.destroy()
        link_filling_content_data(
            root,
            location_content,
            location_header,
            header_height,
            True
        )

    def close() -> None:
        """
        Closing The MINESWEEPER GAME
        """

        mw.destroy()
        root.destroy()

    def on_close() -> None:
        pass

    mw = Toplevel(root, background=PRIMARY)
    mw.resizable(False, False)  # fixed: WIDTH, HEIGHT
    mw.protocol("WM_DELETE_WINDOW", on_close)

    # CENTER
    __width = root.winfo_x() + MW_GEOMETRY
    __height = root.winfo_y() + MW_GEOMETRY
    mw.geometry(f"+{__width}+{__height}")

    label = Label(
        mw,
        foreground=TEXT,
        background=PRIMARY,
        pady=MW_PADY,
        font=font.Font(size=MW_LABEL_FONT_SIZE),
        text=label_text
    )
    label.grid(column=0, columnspan=2, row=0)

    yes_btn = Button(
        mw,
        width=MW_BUTTON_WIDTH,
        foreground=TEXT,
        background=DARK,
        activeforeground=TEXT,
        activebackground=HOVER,
        highlightthickness=1,
        highlightbackground=TEXT,
        borderwidth=0,
        font=font.Font(size=MW_BUTTON_FONT_SIZE),
        text=MW_YES_BUTTON_NAME,
        command=restart
    )
    yes_btn.grid(column=0, row=1, padx=MW_PADY_CONTENT, pady=MW_PADY_CONTENT)

    no_btn = Button(
        mw,
        width=MW_BUTTON_WIDTH,
        foreground=TEXT,
        background=SECONDARY,
        activeforeground=TEXT,
        activebackground=HOVER,
        highlightthickness=1,
        highlightbackground=TEXT,
        borderwidth=0,
        font=font.Font(size=MW_BUTTON_FONT_SIZE),
        text=MW_NO_BUTTON_NAME,
        command=close
    )
    no_btn.grid(column=1, row=1, padx=MW_PADY_CONTENT, pady=MW_PADY_CONTENT)

    mw.transient(root)
    mw.wait_visibility()
    mw.grab_set()
    mw.focus_set()
    mw.wait_window()


# --------------------------------------
