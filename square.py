
import pygame as pg

from constants import SQUARE_WIDTH, SQUARE_HEIGHT


class Square:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.element = pg.Rect(self.x, self.y, SQUARE_WIDTH, SQUARE_HEIGHT)

    def draw(self, screen, color='green'):
        pg.draw.rect(screen, color, self.element)
