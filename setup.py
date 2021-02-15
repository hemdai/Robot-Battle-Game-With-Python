import pygame
import os

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = (WIDTH//COLS)//2
ROBOT_SIZE = (45,25)

# COLORS
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (216,0,0)
BLUE = (0,0,210)
GRAY = (128,128,128)

print("directory is ", os.getcwd())

ROBOTS = {
    "robot1": pygame.transform.scale(pygame.image.load("assets/robot1.png"),ROBOT_SIZE),
    "robot2": pygame.transform.scale(pygame.image.load("assets/robot2.png"), ROBOT_SIZE),
    "robot3": pygame.transform.scale(pygame.image.load("assets/robot3.png"), ROBOT_SIZE)
}

