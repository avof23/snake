
import pygame as pg

from square import Square
from constants import SQUARE_WIDTH, SQUARE_HEIGHT


class Apple(Square):
    def __init__(self, *args):
        super().__init__(*args)

    def moveapple(self, x, y):
        self.x = x
        self.y = y
        self.element = pg.Rect(self.x, self.y, SQUARE_WIDTH, SQUARE_HEIGHT)
