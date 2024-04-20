# Developer && Owner: МогучийДД (MoguchiyDD)
# LICENSE: MIT License which is located in the text file LICENSE
#
# Goal: Create SMALL HELPER FUNCTIONS
# Result: Ready SMALL HELPER FUNCTIONS
#
# Past Modification: Adding COPYRIGHT
# Last Modification: Adding The «HEIGHT» Block
# Modification Date: 2024.04.20, 02:41 PM
#
# Create Date: 2024.04.18, 05:16 PM


from settings import HEIGHT


# ------------ HEIGHT ------------

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

# --------------------------------
