# Developer && Owner: МогучийДД (MoguchiyDD)
# LICENSE: MIT License which is located in the text file LICENSE
#
# Goal: Launch Working SOFTWARE
# Result: Opens The Finished SOFTWARE in The ACTIVE WINDOW
#
# Past Modification: Adding COPYRIGHT
# Last Modification: Adding The «SOFTWARE» Block
# Modification Date: 2024.04.18, 05:17 PM
#
# Create Date: 2024.04.18, 01:03 PM


from tkinter import Tk, Frame

from settings import (
    TITLE,
    WIDTH,
    HEIGHT,
    HEADER_HEIGHT_DIV,
    FOOTER_HEIGHT_DIV,
    PRIMARY,
    DARK
)
from utils import height_div


# ------------ SOFTWARE ------------

root = Tk()

header_height = height_div(HEADER_HEIGHT_DIV)
footer_height = height_div(FOOTER_HEIGHT_DIV)
content_height = HEIGHT - header_height - footer_height

# Settings
root.configure(background=PRIMARY)

root.title(TITLE)
root.geometry(f"{ WIDTH }x{ HEIGHT }")  # set: WIDTHxHEIGHT
root.resizable(False, False)  # fixed: WIDTH, HEIGHT

# Content
header = Frame(
    root,
    background=PRIMARY,
    width=WIDTH,
    height=header_height
)
header.place(x=0, y=0)

content = Frame(
    root,
    background=PRIMARY,
    width=WIDTH,
    height=content_height
)
content.place(x=0, y=header_height)

footer = Frame(
    root,
    background=DARK,
    width=WIDTH,
    height=footer_height
)
footer.place(x=0, y=(content_height + header_height))

# Run
root.mainloop()

# ----------------------------------
