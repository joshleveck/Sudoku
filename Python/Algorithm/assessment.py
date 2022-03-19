import pygame as py
from Helpers.visual import drawFromArray


def assess(solve, org, win, colours, width, font):
    sqWidth = width // 9
    for i in range(9):
        for j in range(9):
            if org[i][j].num() != 0:
                if solve[i][j] == org[i][j].num():
                    py.draw.rect(
                        win,
                        colours["GREEN"],
                        (j * sqWidth, i * sqWidth, sqWidth, sqWidth),
                    )
                else:
                    py.draw.rect(
                        win,
                        colours["RED"],
                        (j * sqWidth, i * sqWidth, sqWidth, sqWidth),
                    )
            else:
                py.draw.rect(
                    win,
                    colours["GREEN"],
                    (j * width, i * width, width, width),
                )
    drawFromArray(solve, colours, win, width, font)
