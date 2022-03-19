import pygame as py
from constants import WIDTH, NAME, FONT, COLOURS, ROWS
from Helpers import input, visual, initial, webscraper
from Algorithm import backtracking, assessment


def main(width, name, fontName, colours, rows):
    win, font = initial.initializeBoard(width, name, fontName)
    board = webscraper.sudoku()
    grid, original = initial.makeGrid(rows, width, board, colours)

    run = True
    started = False

    selected = None
    while run:
        if not started:
            visual.draw(win, grid, rows, width, colours, font)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

            if py.mouse.get_pressed()[0]:
                pos = py.mouse.get_pos()
                selected = input.leftClick(pos, rows, width, grid, original, selected)

            elif py.mouse.get_pressed()[2]:
                pos = py.mouse.get_pos()

            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    started = True
                    solveGrid = original
                    backtracking.solve(solveGrid, win, colours, width, font)
                    visual.drawFromArray(solveGrid, colours, win, width, font)
                    assessment.assess(solveGrid, grid, win, colours, width, font)
                else:
                    selected, started = input.keydown(
                        event.key, grid, original, selected, started
                    )
    py.quit()


main(WIDTH, NAME, FONT, COLOURS, ROWS)
