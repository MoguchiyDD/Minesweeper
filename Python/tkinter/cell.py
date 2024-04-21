# Developer && Owner: МогучийДД (MoguchiyDD)
# LICENSE: MIT License which is located in the text file LICENSE
#
# Goal: Create BOX with CONTENTS
# Result: Ready BOX with CONTENTS
#
# Past Modification: Editing The «CELL» Block (LABELS)
# Last Modification: Bug Fixed
# Modification Date: 2024.04.21, 07:18 PM
#
# Create Date: 2024.04.20, 03:03 PM


from tkinter import Misc, Frame, Label, Button, Event, PhotoImage, font
from random import randint, sample

from settings import (
    CELL_NAME,
    BOMB_NAME,
    MW_LABEL_NAME_WIN,
    MW_LABEL_NAME_LOSE,
    GRID_CELLS,
    CELL_COUNT,
    CELL_WIDTH_LABEL,
    SIZE_CELLS,
    WIDTH_CELL,
    HEIGHT_CELL,
    MIN_BOMB,
    MAX_BOMB,
    SIZE_BOMB,
    HEADER_CELL_FONT_SIZE,
    PRIMARY,
    SECONDARY,
    HOVER,
    TEXT
)
from utils import mw_win_or_lose


# ------------- CELL -------------

class Cell:
    """
    Creates a SINGLE CELL

    ---
    GLOBAL:
    - all -> All CELLS
    - bomb -> All BOMBS
    - bombs_flag -> All FLAGS of BOMBS
    - bombs_flag_true_count -> Number of Correctly Activated FLAGS Above
    BOMBS on The FIELD
    - cell_count_label -> Label for CELLS
    - bomb_count_label -> Label for BOMBS
    - cell_count -> CELL Counting for Label with CELLS
    - bomb_count -> BOMB Counting for Label with BOMBS
    - is_restart -> Permission to RELOAD The HEADER and CONTENT of The SOFTWARE
    - root -> Link to The SOFTWARE that Launches The MAIN WINDOW
    - link_filling_content_data -> Link to «filling_content_data» FUNCTION
    («content/content.py» FILE) that will RESTART and FILL The HEADER and
    CONTENT in The SOFTWARE with New DATA
    - frame_content = Link to The SOFTWARE of CONTENT
    - frame_header = Link to The SOFTWARE of HEADER
    - header_heigh = Link to The SOFTWARE of HEADER HEIGHT
    ---
    PARAMETERS:
    - x: int -> X Axis of The CURRENT CELL
    - y: int -> Y Axis of The CURRENT CELL
    - is_opened: bool = False -> The CELL is Opened by The USER
    - is_bomb: bool = False -> The CELL will be a BOMB
    - is_bomb_flag: bool = False -> The USER Clicked on The RIGHT MOUSE BUTTON
    to Color a BLOCK (LIKE THERE IS A BOMB)
    ---
    FUNCTIONS:
    - create_cell_btn(location: Frame) -> None : Creates a BUTTON and Binds
    it to The «cell_btn» Variable
    - show_bombs() -> None : Shows a BOMBS on The FIELD
    - show_cell() -> None : Shows a CELL on The FIELD
    - get_cell_by_axis(x: int, y: int) -> None | object :
    Using The X and Y Axes, it Finds The Desired CELL
    - active_mw(label_text: str) -> None : Activates a MODAL WINDOW
    ---
    STATICS:
    - create_cell_count_label(location: Frame) -> None : Creates a LABEL and
    Binds it to The «cell_count_label» Class Variable
    - create_bomb_count_label(location: Frame) -> None : Creates a LABEL and
    Binds it to The «bomb_count_label» Class Variable
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
    - mouse_right_click(_: Event) -> None : Reacts when RIGHT-CLICKED
    ---
    OTHER:
    - __repr__() -> str : Replaces The IDs of CLASS «Cell» with a STRING
    """

    # Total
    all = []
    bombs = []
    bombs_flag = []
    bombs_flag_true_count = 0

    # Labels
    cell_count_label = None
    bomb_count_label = None
    cell_count = CELL_COUNT
    bomb_count = 0

    # For Restart
    is_restart = False
    root = None
    link_filling_content_data = None
    frame_content = None
    frame_header = None
    header_heigh = None

    def __init__(
        self,
        x: int, y: int,
        is_opened: bool = False,
        is_bomb: bool = False,
        is_bomb_flag: bool = False
    ) -> None:
        self.x = x
        self.y = y
        self.is_opened = is_opened
        self.is_bomb = is_bomb
        self.is_bomb_flag = is_bomb_flag

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

    @staticmethod
    def create_cell_count_label(location: Frame) -> None:
        """
        Creates a LABEL and Binds it to The «cell_count_label» Class Variable

        ---
        PARAMETERS:
        - location: Frame -> Location for The LABEL
        """

        label = Label(
            location,
            anchor="ne",
            width=CELL_WIDTH_LABEL,
            foreground=TEXT,
            background=PRIMARY,
            text=f"{ CELL_NAME }{ Cell.cell_count }",
            font=font.Font(size=HEADER_CELL_FONT_SIZE)
        )

        Cell.cell_count_label = label

    @staticmethod
    def create_bomb_count_label(location: Frame) -> None:
        """
        Creates a LABEL and Binds it to The «bomb_count_label» Class Variable

        ---
        PARAMETERS:
        - location: Frame -> Location for The LABEL
        """

        label = Label(
            location,
            foreground=TEXT,
            background=PRIMARY,
            text=f"{ BOMB_NAME }{ Cell.bomb_count }",
            font=font.Font(size=HEADER_CELL_FONT_SIZE)
        )

        Cell.bomb_count_label = label

    def mouse_left_click(self, _: Event) -> None:
        """
        Reacts when LEFT-CLICKED

        ---
        PARAMETERS:
        - _: Event -> Link with BUTTON
        """

        if (self.is_bomb) and (not self.is_bomb_flag):  # Click BOMB
            self.show_bombs()
            self.active_mw(MW_LABEL_NAME_LOSE)
        elif (not self.is_bomb) and (not self.is_bomb_flag):  # Click CELL
            self.show_cell()

            # At 0, Opens All CELLS Up to The 2nd ROW of NUMBERS
            if self.surrounded_cells_bombs_length == 0:
                neighbours = self.surrounded_cells
                for neighbour in neighbours:
                    x, self.x = self.x, neighbour.x
                    y, self.y = self.y, neighbour.y

                    if not neighbour.is_bomb_flag:
                        neighbour.show_cell()
                        if self.surrounded_cells_bombs_length == 0:
                            for cell in self.surrounded_cells:
                                if cell not in neighbours:
                                    neighbours.append(cell)

                    self.x = x
                    self.y = y

    def mouse_right_click(self, _: Event) -> None:
        """
        Reacts when RIGHT-CLICKED

        ---
        PARAMETERS:
        - _: Event -> Link with BUTTON
        """

        if (not self.is_bomb_flag) and (Cell.bomb_count >= 1):  # Set Flag
            self.cell_btn.configure(
                foreground=TEXT,
                background=TEXT,
                activeforeground=TEXT,
                activebackground=TEXT
            )
            self.is_bomb_flag = True
        elif (self.is_bomb_flag) and (self.is_opened):  # Remove Flag (YES)
            self.cell_btn.configure(
                activebackground=HOVER,
                font=font.Font(size=SIZE_CELLS),
                text=self.surrounded_cells_bombs_length
            )
            if self.surrounded_cells_bombs_length == 0:  # Bomb 0
                self.cell_btn.configure(
                    foreground=HOVER,
                    background=HOVER,
                    activeforeground=HOVER
                )
            else:  # More Bombs
                self.cell_btn.configure(
                    foreground=TEXT,
                    background=HOVER,
                    activeforeground=TEXT
                )
            self.is_bomb_flag = False
        elif (self.is_bomb_flag) and (not self.is_opened):  # Remove Flag (NO)
            self.cell_btn.configure(
                foreground=SECONDARY,
                background=SECONDARY,
                activeforeground=HOVER,
                activebackground=HOVER
            )
            self.is_bomb_flag = False

        # LIST with BOMBS of FLAGS (for LABELS)
        if self.is_bomb_flag:
            Cell.bomb_count -= 1
            Cell.bombs_flag.append(self)  # for MODAL WINDOW
        else:
            Cell.bomb_count += 1
            if self in Cell.bombs_flag:  # for MODAL WINDOW
                Cell.bombs_flag.remove(self)

        # LABEL : BOMBS
        if Cell.bomb_count_label:
            Cell.bomb_count_label.configure(
                text=f"{ BOMB_NAME }{ Cell.bomb_count }",
            )

        # Modal Window
        if Cell.bomb_count == 0:  # No BOMBS
            for flag in Cell.bombs_flag:  # (FLAG == BOMB) <—> COUNT
                if flag.is_bomb:
                    Cell.bombs_flag_true_count += 1

            if Cell.bombs_flag_true_count == len(Cell.bombs):  # WIN
                self.active_mw(MW_LABEL_NAME_WIN)

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

        # LABEL : CELLS
        if (Cell.cell_count_label) and (self.is_opened is False):
            if Cell.is_restart:
                Cell.cell_count = CELL_COUNT
            else:
                Cell.cell_count -= 1
            Cell.cell_count_label.configure(
                text=f"{ CELL_NAME }{ Cell.cell_count }"
            )

        self.is_opened = True  # OPENED CELL

        # BUTTON
        self.cell_btn.configure(  # Picked TOTAL
            background=HOVER,
            activebackground=HOVER,
            font=font.Font(size=SIZE_CELLS)
        )

        if self.surrounded_cells_bombs_length != 0:  # Picked All (but 0)
            self.cell_btn.configure(
                foreground=TEXT,
                activeforeground=TEXT,
                text=self.surrounded_cells_bombs_length
            )
        else:  # Picked 0
            self.cell_btn.configure(
                foreground=HOVER,
                activeforeground=HOVER,
                text=self.surrounded_cells_bombs_length
            )

        # WIN
        if Cell.cell_count <= 0:
            self.active_mw(MW_LABEL_NAME_WIN)

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

        # X and Y Axises <= -1 && X and Y Axises >= 9
        if (((x <= -1) or (y <= -1)) and
                (((x >= GRID_CELLS) or (y >= GRID_CELLS)))):
            return None

        # Picked 1 CELL
        picked_cell = None
        for cell in Cell.all:
            if (cell.x == x) and (cell.y == y):
                picked_cell = cell
                break

        return picked_cell

    @staticmethod
    def randomize_bomb() -> None:
        """
        Installing BOMBS in Different CELLS
        """

        # Restart The MINESWEEPER GAME
        if len(Cell.all) and len(Cell.bombs):
            for cell in Cell.all:  # All CELLS
                cell.is_opened = False
                cell.is_bomb_flag = False

            for bomb in Cell.bombs:  # All BOMBS
                bomb.is_bomb = False
                bomb.is_bomb_flag = False

            Cell.bombs = []
            Cell.bombs_flag = []
            Cell.bombs_flag_true_count = 0

        # Set BOMBS
        bomb_count = randint(MIN_BOMB, MAX_BOMB)
        Cell.bombs = sample(Cell.all, bomb_count)
        for bomb in Cell.bombs:
            bomb.is_bomb = True

        # LABEL : BOMBS and CELLS
        if (Cell.bomb_count_label) and (Cell.cell_count_label):
            len_bombs = len(Cell.bombs)

            # BOMBS
            if Cell.is_restart:
                Cell.bomb_count = len_bombs
            else:
                Cell.bomb_count += len_bombs
            Cell.bomb_count_label.configure(
                text=f"{ BOMB_NAME }{ Cell.bomb_count }",
            )

            # CELLS
            if Cell.is_restart:
                Cell.cell_count = CELL_COUNT - len_bombs
            else:
                Cell.cell_count -= len_bombs
            Cell.cell_count_label.configure(
                text=f"{ CELL_NAME }{ Cell.cell_count }"
            )

    def active_mw(self, label_text: str) -> None:
        """
        Activates a MODAL WINDOW

        ---
        PARAMETERS:
        - label_text: str -> Text for MODAL WINDOW
        """

        mw_win_or_lose(
            label_text,
            Cell.root,
            Cell.link_filling_content_data,
            Cell.frame_content,
            Cell.frame_header,
            Cell.header_height
        )

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
