import pygame as py


def drawGrid(win, rows, width, colours):
    gap = width // rows
    for i in range(rows):
        if i % 3 == 0:
            py.draw.line(win, colours["BLACK"], (0, i * gap), (width, i * gap), width=3)
        else:
            py.draw.line(win, colours["GREY"], (0, i * gap), (width, i * gap))
    for j in range(rows):
        if j % 3 == 0:
            py.draw.line(win, colours["BLACK"], (j * gap, 0), (j * gap, width), width=3)
        else:
            py.draw.line(win, colours["GREY"], (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width, colours, font):
    win.fill(colours["WHITE"])
    for row in grid:
        for sq in row:
            sq.draw(win, font)
    drawGrid(win, rows, width, colours)
    py.display.update()


def drawFromArray(board, colours, win, width, font):
    sqWidth = width // 9
    for i in range(9):
        for j in range(9):
            value = str(board[i][j])
            text = font.render(value, True, colours["BLACK"])
            textRect = text.get_rect(
                center=(
                    j * sqWidth + sqWidth / 2,
                    i * sqWidth + sqWidth / 2,
                )
            )
            win.blit(text, textRect)
    drawGrid(win, 9, width, colours)
    py.display.update()
