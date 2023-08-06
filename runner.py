# Example file showing a basic pygame "game loop"
import random

import pygame

from constants import WIDTH, HEIGHT, SQUARE_WIDTH, SQUARE_HEIGHT, SNAKE_DELAY_SPEED, GAME_OVER_TIMEOUT, REFRESH_SCREEN
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
random.seed()
snake = Snake(*generate_xy())
apple = Apple(*generate_xy())

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    success_moving = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                vector = 'UP'
            #    success_moving = snake.move(pygame.K_UP)
            if event.key == pygame.K_DOWN:
                vector = 'DOWN'
            #    success_moving = snake.move(pygame.K_DOWN)
            if event.key == pygame.K_RIGHT:
                vector = 'RIGHT'
            #    success_moving = snake.move(pygame.K_RIGHT)
            if event.key == pygame.K_LEFT:
                vector = 'LEFT'
            #    success_moving = snake.move(pygame.K_LEFT)

    success_moving = snake.move_vector(vector)
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    if not success_moving:
        snake.draw(screen, color='orange')
        running = False
    elif apple.x == snake.x and apple.y == snake.y:
        pass
        # Проверить чтоб не генерировать яблоко внутри хвоста !
        apple.moveapple(*generate_xy())
        apple.draw(screen, color='red')
        snake.add_tail(vector)
        snake.draw(screen)
    else:
        apple.draw(screen, color='red')
        snake.draw(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.time.delay(SNAKE_DELAY_SPEED)
    clock.tick(REFRESH_SCREEN)

pygame.time.delay(GAME_OVER_TIMEOUT)
pygame.quit()
