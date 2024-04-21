# Developer && Owner: МогучийДД (MoguchiyDD)
# LICENSE: MIT License which is located in the text file LICENSE
#
# Goal: Launch Working SOFTWARE
# Result: Opens The Finished SOFTWARE in The ACTIVE WINDOW
#
# Past Modification: Bug Fixed
# Last Modification: Centralization of The SOFTWARE WINDOW
# Modification Date: 2024.04.21, 06:43 PM
#
# Create Date: 2024.04.20, 03:03 PM


from tkinter import Tk

from content.header import header
from content.content import content
from content.footer import footer, footer_copyright

from settings import TITLE, WIDTH, HEIGHT, PRIMARY

from sys import path as syspath
syspath.append(__file__)


# ------------ SOFTWARE ------------

root = Tk()

# CENTER WINDOW
x = (root.winfo_screenwidth() - WIDTH) // 2
y = (root.winfo_screenheight() - HEIGHT) // 2

# Settings
root.configure(background=PRIMARY)

root.title(TITLE)
root.geometry(f"{ WIDTH }x{ HEIGHT }+{ x }+{ y }")
root.resizable(False, False)  # fixed: WIDTH, HEIGHT

# Content : HEADER
func_header = header(root)
frame_header = func_header[0]
header_height = func_header[1]

# Content : CONTENT
content(root, frame_header)

# Content : FOOTER
func_footer = footer(root)
frame_footer = func_footer[0]
footer_height = func_footer[1]
footer_copyright(frame_footer, footer_height)

# Run
root.mainloop()

# ----------------------------------
