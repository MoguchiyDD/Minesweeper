# Developer && Owner: МогучийДД (MoguchiyDD)
# LICENSE: MIT License which is located in the text file LICENSE
#
# Goal: Create BOX with CONTENTS
# Result: Ready BOX with CONTENTS
#
# Past Modification: Adding COPYRIGHT
# Last Modification: Adding The «CELL» Block
# Modification Date: 2024.04.18, 07:00 PM
#
# Create Date: 2024.04.18, 05:26 PM


from tkinter import Frame, Button, Event


# ------------ CELL ------------

class Cell:
    """
    Creates a SINGLE CELL

    ---
    PARAMETERS:
    - is_bomb: bool = False -> The CELL will be a BOMB
    ---
    FUNCTIONS:
    - create_cell_btn(location: Frame) -> None : Creates a BUTTON and Binds
    it to The «cell_btn» Variable
    ---
    EVENTS:
    - mouse_left_click(event: Event) -> None : Reacts when LEFT-CLICKED
    - mouse_right_click(event: Event) -> None : Reacts when RIGHT-CLICKED
    """

    def __init__(self, is_bomb: bool = False) -> None:
        self.is_bomb = is_bomb
        self.cell_btn = None

    def create_cell_btn(self, location: Frame) -> None:
        """
        Creates a BUTTON and Binds it to The «cell_btn» Variable

        ---
        PARAMETERS:
        - location: Frame -> Location for The BUTTON
        """

        btn = Button(
            location,
            text="Text"
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

# ------------------------------
