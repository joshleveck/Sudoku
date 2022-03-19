def getClickedPos(pos, rows, width):
    gap = width // rows
    y, x = pos

    col = y // gap
    row = x // gap

    return col, row
