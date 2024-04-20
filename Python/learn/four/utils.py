# Developer && Owner: МогучийДД (MoguchiyDD)
# LICENSE: MIT License which is located in the text file LICENSE
#
# Goal: Create SMALL HELPER FUNCTIONS
# Result: Ready SMALL HELPER FUNCTIONS
#
# Past Modification: Adding The «HEIGHT» Block
# Last Modification: Adding The «FRAME HEIGHT» Block
# Modification Date: 2024.04.20, 01:06 PM
#
# Create Date: 2024.04.19, 07:24 PM


from settings import HEIGHT, HEADER_HEIGHT_DIV, FOOTER_HEIGHT_DIV


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
