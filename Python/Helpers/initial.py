import pygame as py
import Classes.Square as Square


def initializeBoard(width, name, font):
    win = py.display.set_mode((width, width))
    py.display.set_caption(name)
    py.font.init()
    font = py.font.SysFont(font, 50)
    return win, font


def makeGrid(rows, width, board, colours):
    grid = []
    gap = width // rows
    sudoku = board
    original = []
    for i in range(rows):
        grid.append([])
        original.append([])
        for j in range(rows):
            value = sudoku[i][j]
            sq = Square.Square(value, j, i, gap, colours)
            original[i].append(value)
            grid[i].append(sq)

    return grid, original
