import Helpers.translator as translator
import pygame as py


def leftClick(pos, rows, width, grid, original, selected):
    col, row = translator.getClickedPos(pos, rows, width)
    sq = grid[row][col]
    if sq in original:
        pass
    else:
        if selected != None:
            selected.clear()
        selected = sq
        selected.selected()
    return selected


def rightClick(pos, rows, width, grid, original):
    col, row = translator.getClickedPos(pos, rows, width)
    sq = grid[row][col]
    if sq in original:
        pass
    else:
        sq.setValue(0)


def keydown(key, grid, original, selected, started):
    if key == py.K_r:
        started = False
        for row in grid:
            for sq in row:
                if sq in original:
                    pass
                else:
                    sq.setValue(0)

    if selected != None:
        if key == py.K_0:
            selected.setValue(0)
            selected.clear()
            selected = None
        if key == py.K_1:
            selected.setValue(1)
            selected.clear()
            selected = None
        if key == py.K_2:
            selected.setValue(2)
            selected.clear()
            selected = None
        if key == py.K_3:
            selected.setValue(3)
            selected.clear()
            selected = None
        if key == py.K_4:
            selected.setValue(4)
            selected.clear()
            selected = None
        if key == py.K_5:
            selected.setValue(5)
            selected.clear()
            selected = None
        if key == py.K_6:
            selected.setValue(6)
            selected.clear()
            selected = None
        if key == py.K_7:
            selected.setValue(7)
            selected.clear()
            selected = None
        if key == py.K_8:
            selected.setValue(8)
            selected.clear()
            selected = None
        if key == py.K_9:
            selected.setValue(9)
            selected.clear()
            selected = None

    return selected, started
