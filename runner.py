# Example file showing a basic pygame "game loop"
import random

import pygame

from constants import WIDTH, HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT, SNAKE_DELAY_SPEED, GAME_OVER_TIMEOUT, REFRESH_SCREEN, START_SNAKE_W, START_SNAKE_H
from snake import Snake
from apple import Apple


def generate_xy():
    return random.randrange(0, WIDTH - SQUARE_WIDTH, SQUARE_WIDTH), random.randrange(0, HEIGHT - SQUARE_HEIGHT, SQUARE_HEIGHT)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()
running = True
vector = 'RIGHT'
acceleration = 0
random.seed()
snake = Snake(START_SNAKE_W,START_SNAKE_H)
apple = Apple(*generate_xy())

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    success_moving = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and vector != 'DOWN':
                vector = 'UP'
            if event.key == pygame.K_DOWN and vector != 'UP':
                vector = 'DOWN'
            if event.key == pygame.K_RIGHT and vector != 'LEFT':
                vector = 'RIGHT'
            if event.key == pygame.K_LEFT and vector != 'RIGHT':
                vector = 'LEFT'

    success_moving = snake.move_vector(vector)
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    if not success_moving:
        snake.draw(screen, color='orange')
        running = False
    elif apple.x == snake.x and apple.y == snake.y:
        while snake.in_snake(*(applexy := generate_xy())):
            pass
        acceleration -= 5
        apple.moveapple(*applexy)
        apple.draw(screen, color='red')
        snake.add_tail(vector)
        snake.draw(screen)
    else:
        apple.draw(screen, color='red')
        snake.draw(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.time.delay(SNAKE_DELAY_SPEED + acceleration)
    clock.tick(REFRESH_SCREEN)

pygame.time.delay(GAME_OVER_TIMEOUT)
pygame.quit()
