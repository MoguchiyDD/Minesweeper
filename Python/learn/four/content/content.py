# Developer && Owner: МогучийДД (MoguchiyDD)
# LICENSE: MIT License which is located in the text file LICENSE
#
# Goal: SOFTWARE CONTENT
# Result: Ready SOFTWARE CONTENT
#
# Past Modification: Adding COPYRIGHT
# Last Modification: Moving The CONTENT from «main.py» to «content/content.py»
# Modification Date: 2024.04.21, 08:03 AM
#
# Create Date: 2024.04.20, 01:12 PM


from tkinter import Tk, Frame

from settings import WIDTH, PRIMARY
from utils import frame_header, frame_content


# ------------ CONTENT ------------

def content(root: Tk) -> Frame:
    """
    Responsible for Drawing in The SOFTWARE CONTENT

    ---
    PARAMETERS:
    - root: Tk -> SOFTWARE WINDOW
    ---
    RESULTS: CONTENT
    """

    header_height = frame_header()
    content_height = frame_content()

    content = Frame(
        root,
        background=PRIMARY,
        width=WIDTH,
        height=content_height
    )
    content.place(x=0, y=header_height)

    return content

# ---------------------------------
