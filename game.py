import pygame
from grid import Grid
from setup import (
    RED, BLUE, BLACK, WHITE
)

class Game:

    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.grid.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected_robot = None
        self.grid = Grid()
        self.turn = RED
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected_robot:
            result = self._move(row, col)
            if not result:
                self.selected_robot = None
                self.select(row, col)
        else:
            robot = self.grid.get_robot(row, col)
            if robot != 0 and self.robot.color.turn:
                self.selected_robot = robot
                self.valid_moves = self.grid_valid_moves(robot)
                return True
        return False

    def _move(self, row, col):
        robot = self.grid.get_robot(row, col)
        if self.selected_robot and robot == 0 and (row, col) in self.valid_moves:
            self.grid.move(self.selected_robot, row, col)

        else:
            return False

        return True

    def change_turn(self):
        if self.turn == RED:
            self.turn == WHITE
        else:
            self.turn = RED



