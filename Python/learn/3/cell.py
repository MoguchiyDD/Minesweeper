# Developer && Owner: МогучийДД (MoguchiyDD)
# LICENSE: MIT License which is located in the text file LICENSE
#
# Goal: Create BOX with CONTENTS
# Result: Ready BOX with CONTENTS
#
# Past Modification: Editing The «CELL» Block (STYLE, BOMBS && CELLS)
# Last Modification: Adding The «UPDATE» Block
# Modification Date: 2024.04.19, 07:05 PM
#
# Create Date: 2024.04.19, 01:04 PM


from tkinter import Misc, Frame, Button, Event, PhotoImage, font
from random import randint, sample

from settings import (
    GRID_CELLS,
    SIZE_CELLS,
    WIDTH_CELL,
    HEIGHT_CELL,
    MIN_BOMB,
    MAX_BOMB,
    SIZE_BOMB,
    PRIMARY,
    SECONDARY,
    HOVER,
    TEXT
)


# ------------- CELL -------------

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
    - show_bombs() -> None : Shows a BOMBS on The FIELD
    - show_cell() -> None : Shows a CELL on The FIELD
    - get_cell_by_axis(x: int, y: int) -> None | object :
    Using The X and Y Axes, it Finds The Desired CELL
    ---
    STATICS:
    - randomize_bomb() -> None : Installing BOMBS in Different CELLS
    ---
    PROPERTY:
    - surrounded_cells() -> list[object] : From The CURRENT CELL, Finds CELLS
    Located Around The CURRENT CELL itself (NEIGHBORS)
    - surrounded_cells_bombs_length() -> int : From a List with
    SURROUNDING CELLS, Finds BOMBS and COUNTS their NUMBER
    ---
    EVENTS:
    - mouse_left_click(_: Event) -> None : Reacts when LEFT-CLICKED
    - mouse_right_click(event: Event) -> None : Reacts when RIGHT-CLICKED
    ---
    OTHER:
    - __repr__() -> str : Replaces The IDs of CLASS «Cell» with a STRING
    """

    all = []
    bombs = []

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

        btn = tkButton(
            location,
            foreground=SECONDARY,
            background=SECONDARY,
            activeforeground=HOVER,
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

    def mouse_left_click(self, _: Event) -> None:
        """
        Reacts when LEFT-CLICKED

        ---
        PARAMETERS:
        - _: Event -> Link with BUTTON
        """

        if self.is_bomb:
            self.show_bombs()
        else:
            self.show_cell()

    def mouse_right_click(self, event: Event) -> None:
        """
        Reacts when RIGHT-CLICKED

        ---
        PARAMETERS:
        - event: Event -> Link with BUTTON
        """

        print(event, "\t", "MOUSE: Right Click")

    def show_bombs(self) -> None:
        """
        Shows a BOMBS on The FIELD
        """

        for bomb in Cell.bombs:
            bomb.cell_btn.configure(
                foreground=PRIMARY,
                background=TEXT,
                activeforeground=PRIMARY,
                activebackground=TEXT,
                font=font.Font(size=SIZE_BOMB),
                text="☢"
            )

    def show_cell(self) -> None:
        """
        Shows a CELL on The FIELD
        """

        self.cell_btn.configure(
            foreground=TEXT,
            background=HOVER,
            activeforeground=TEXT,
            activebackground=HOVER,
            font=font.Font(size=SIZE_CELLS),
            text=self.surrounded_cells_bombs_length
        )

    @property
    def surrounded_cells(self) -> list[object]:
        """
        From The CURRENT CELL, Finds CELLS Located Around The CURRENT CELL
        itself (NEIGHBORS)
        ---
        RESULTS: List with SURROUNDING CELLS
        """

        cells = [
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x - 1, self.y - 1)
        ]
        cells = [cell for cell in cells if cell is not None]

        return cells

    @property
    def surrounded_cells_bombs_length(self) -> int:
        """
        From a List with SURROUNDING CELLS, Finds BOMBS and COUNTS
        their NUMBER
        ---
        RESULTS: NUMBER of BOMBS in SURROUNDING CELLS
        """

        bomb_count = 0
        for cell in self.surrounded_cells:
            if cell.is_bomb:
                bomb_count += 1

        return bomb_count

    def get_cell_by_axis(self, x: int, y: int) -> None | object:
        """
        Using The X and Y Axes, it Finds The Desired CELL

        ---
        PARAMETETS:
        - x: int -> X Axis of The CURRENT CELL
        - y: int -> Y Axis of The CURRENT CELL
        ---
        RESULTS: Found CELL or Nothing
        """

        if (((x <= -1) or (y <= -1)) and
                (((x >= GRID_CELLS) or (y >= GRID_CELLS)))):
            return None

        for cell in Cell.all:
            if (cell.x == x) and (cell.y == y):
                return cell

    @staticmethod
    def randomize_bomb() -> None:
        """
        Installing BOMBS in Different CELLS
        """

        bomb_count = randint(MIN_BOMB, MAX_BOMB)
        Cell.bombs = sample(Cell.all, bomb_count)
        for bomb in Cell.bombs:
            bomb.is_bomb = True

    def __repr__(self) -> str:
        """
        Replaces The IDs of CLASS «Cell» with a STRING

        ---
        RESULTS: Cell(e.g. 8, e.g 8) | 1st — x ; 2nd — y
        """

        result = f"Cell({ self.x }, { self.y })"
        return result

# --------------------------------


# ------------ UPDATE ------------

class tkButton(Button):
    def __init__(self, master: Misc | None = None, **kwargs):
        self.img = PhotoImage()
        Button.__init__(
            self,
            master,
            image=self.img,
            compound='center',
            **kwargs
        )

# --------------------------------
