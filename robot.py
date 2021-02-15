from setup import BLUE, WHITE, SQUARE_SIZE, GRAY, ROBOTS
import pygame

class Robot:
    PADDING = 10
    OUTLINE = 2


    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.robot1 = False
        self.robot2 = False
        self.robot3 = True

        self.x = 0
        self.y = 0
        self.calc_position()

    def calc_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE//2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE//2

    def make_robot1(self):
        self.robot1 = True

    def make_robot2(self):
        self.robot2 = True

    def make_robot3(self):
        self.robot3 = True

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, self.color, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.make_robot1:
            win.blit(ROBOTS['robot1'], (self.x - ROBOTS['robot1'].get_width()//2, self.y-ROBOTS['robot1'].get_height()//2))

        if self.make_robot2:
            win.blit(ROBOTS['robot2'], (self.x - ROBOTS['robot2'].get_width()//2, self.y-ROBOTS['robot2'].get_height()//2))

        if self.make_robot3:
            win.blit(ROBOTS['robot3'], (self.x - ROBOTS['robot3'].get_width()//2, self.y-ROBOTS['robot3'].get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_position()



    def __repr__(self):
        return str(self.color)

