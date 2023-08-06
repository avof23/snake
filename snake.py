import pygame as pg

from square import Square
from constants import SQUARE_WIDTH, SQUARE_HEIGHT, INIT_COUNT, WIDTH, HEIGHT


class Snake(Square):
    def __init__(self, *args):
        super().__init__(*args)
        self.body = []
        self.body_count = INIT_COUNT
        for i in range(INIT_COUNT):
            self.body.append(pg.Rect(self.x-SQUARE_WIDTH*i, self.y, SQUARE_WIDTH, SQUARE_HEIGHT))

    def draw(self, screen, color='green'):
        for body_element in self.body:
            pg.draw.rect(screen, color, body_element)

    def move_vector(self, vector):
        if vector == 'UP':
            self.y -= SQUARE_HEIGHT
        if vector == 'DOWN':
            self.y += SQUARE_HEIGHT
        if vector == 'RIGHT':
            self.x += SQUARE_WIDTH
        if vector == 'LEFT':
            self.x -= SQUARE_WIDTH
        # print(f'My position {self.x}, {self.y}')
        for i in range(self.body_count-1, -1, -1):
            if i == 0:
                self.body[i] = pg.Rect(self.x, self.y, SQUARE_WIDTH, SQUARE_HEIGHT)
                if self.body[i] in self.body[1:self.body_count]:
                    return False
                if self.x not in range(0, WIDTH-SQUARE_WIDTH+1) or self.y not in range(0, HEIGHT-SQUARE_HEIGHT+1):
                    return False
            else:
                self.body[i] = self.body[i-1]
        return True

    def add_tail(self, vector):
        pass
        self.body_count += 1
        if vector == 'UP' or vector == 'DOWN':
            self.body.append(pg.Rect(self.x, self.y+SQUARE_WIDTH, SQUARE_WIDTH, SQUARE_HEIGHT))
        elif vector == 'LEFT' or vector == 'RIGHT':
            self.body.append(pg.Rect(self.x + SQUARE_WIDTH, self.y, SQUARE_WIDTH, SQUARE_HEIGHT))
