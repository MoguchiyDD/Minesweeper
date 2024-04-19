# Developer && Owner: МогучийДД (MoguchiyDD)
# LICENSE: MIT License which is located in the text file LICENSE
#
# Goal: Create BOX with CONTENTS
# Result: Ready BOX with CONTENTS
#
# Past Modification: Editing The «CELL» Block (STYLE && BOMBS)
# Last Modification: Editing The «CELL» Block (COMMENTS && SPACES)
# Modification Date: 2024.04.19, 07:04 PM
#
# Create Date: 2024.04.18, 07:06 PM


from tkinter import Frame, Button, Event
from random import randint, sample

from settings import (
    WIDTH_CELL,
    HEIGHT_CELL,
    MIN_BOMB,
    MAX_BOMB,
    PRIMARY,
    SECONDARY,
    HOVER,
    TEXT
)


# ------------ CELL ------------

class Cell:
    """
    Creates a SINGLE CELL

    ---
    PARAMETERS:
    - x: int -> X Axis of The CURRENT CELL
    - y: int -> Y Axis of The CURRENT CELL
    - is_bomb: bool = False -> The CELL will be a BOMB
    ---
    FUNCTIONS:
    - create_cell_btn(location: Frame) -> None : Creates a BUTTON and Binds
    it to The «cell_btn» Variable
    ---
    STATICS:
    - randomize_bomb() -> None : Installing BOMBS in Different CELLS
    ---
    EVENTS:
    - mouse_left_click(event: Event) -> None : Reacts when LEFT-CLICKED
    - mouse_right_click(event: Event) -> None : Reacts when RIGHT-CLICKED
    """

    all = []

    def __init__(self, x: int, y: int, is_bomb: bool = False) -> None:
        self.x = x
        self.y = y
        self.is_bomb = is_bomb

        self.cell_btn = None
        Cell.all.append(self)

    def create_cell_btn(self, location: Frame) -> None:
        """
        Creates a BUTTON and Binds it to The «cell_btn» Variable

        ---
        PARAMETERS:
        - location: Frame -> Location for The BUTTON
        """

        btn = Button(
            location,
            foreground=SECONDARY,
            background=SECONDARY,
            activeforeground=TEXT,
            activebackground=HOVER,
            highlightthickness=1,
            highlightbackground=PRIMARY,
            borderwidth=0,
            width=WIDTH_CELL,
            height=HEIGHT_CELL,
            text=f"{ self.x }, { self.y }"
        )
        btn.bind("<Button-1>", self.mouse_left_click)
        btn.bind("<Button-3>", self.mouse_right_click)
        self.cell_btn = btn

    def mouse_left_click(self, event: Event) -> None:
        """
        Reacts when LEFT-CLICKED

        ---
        PARAMETERS:
        - event: Event -> Link with BUTTON
        """

        print(event, "\t", "MOUSE: Left Click")

    def mouse_right_click(self, event: Event) -> None:
        """
        Reacts when RIGHT-CLICKED

        ---
        PARAMETERS:
        - event: Event -> Link with BUTTON
        """

        print(event, "\t", "MOUSE: Right Click")

    @staticmethod
    def randomize_bomb() -> None:
        """
        Installing BOMBS in Different CELLS
        """

        bomb_count = randint(MIN_BOMB, MAX_BOMB)
        picked_cells = sample(Cell.all, bomb_count)
        for picked_cell in picked_cells:
            picked_cell.is_bomb = True

    def __repr__(self) -> str:
        """
        Replaces The IDs of CLASS «Cell» with a STRING

        ---
        RESULTS: Cell(e.g. 8, e.g 8) | 1st — x ; 2nd — y
        """

        result = f"Cell({ self.x }, { self.y })"
        return result

# ------------------------------
