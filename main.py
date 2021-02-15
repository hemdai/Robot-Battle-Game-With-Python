import pygame
from setup import (
    WIDTH, HEIGHT, SQUARE_SIZE
)
from grid import Grid
from game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robots Fights")

def get_row_col_from_mouse(pos):
    x, y  = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)


    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)



        game.update()

    pygame.quit()

main()

