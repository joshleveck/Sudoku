import pygame as py


class Square:
    def __init__(self, value, col, row, width, colours):
        self.value = value
        self.col = col
        self.row = row
        self.width = width
        self.focus = False
        self.colours = colours

    def draw(self, win, font):
        if self.focus:
            py.draw.rect(
                win,
                self.colours["SELECTED"],
                (self.col * self.width, self.row * self.width, self.width, self.width),
            )
        else:
            py.draw.rect(
                win,
                self.colours["WHITE"],
                (self.col * self.width, self.row * self.width, self.width, self.width),
            )
        if self.value == 0:
            return
        value = str(self.value)
        text = font.render(value, True, self.colours["BLACK"])
        textRect = text.get_rect(
            center=(
                self.col * self.width + self.width / 2,
                self.row * self.width + self.width / 2,
            )
        )
        win.blit(text, textRect)

    def setValue(self, value):
        self.value = value

    def selected(self):
        self.focus = True

    def clear(self):
        self.focus = False

    def num(self):
        return self.value
