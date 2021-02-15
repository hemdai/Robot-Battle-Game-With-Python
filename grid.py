import pygame
from setup import BLACK, ROWS, COLS, RED, SQUARE_SIZE, WHITE, BLUE
from robot import Robot


class Grid:
    def __init__(self):
        self.grid = []
        self.red_left = self.white_left = 12
        self.blue_robots = self.white_robots = 0
        self.create_grid()

    def draw_shell(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BLUE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, robot, row, col):
        self.grid[robot.row][robot.col], self.grid[row][col] = self.grid[row][col], self.grid[robot.row][robot.col]
        robot.move(row, col)

        if row == ROWS - 1 or row == 0:
            robot.make_robot1()
            if robot.color == BLUE:
                self.blue_robots += 1
            else:
                self.white_robots += 1

    def get_robot(self, row, col):
        return self.grid[row][col]

    def create_grid(self):
        for row in range(ROWS):
            self.grid.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.grid[row].append(Robot(row, col, RED))
                    elif row > 4:
                        self.grid[row].append(Robot(row, col, BLACK))
                    else:
                        self.grid[row].append(0)
                else:
                    self.grid[row].append(0)

    def draw(self, win):
        self.draw_shell(win)
        for row in range(ROWS):
            for col in range(COLS):
                robot = self.grid[row][col]
                if robot != 0:
                    robot.draw(win)

    def get_valid_moves(self, robot):
        moves = {}
        left = robot.col - 1
        right = robot.col + 1
        row = robot.row

        if robot.color == RED or robot.robot1:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, robot.color, left))
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, robot.color, right))
        if robot.color == BLACK or robot.robot1:
            moves.update(self._traverse_left(row + 1, max(row + 3, ROWS), 1, robot.color, left))
            moves.update(self._traverse_left(row + 1, max(row + 3, ROWS), 1, robot.color, right))
        if robot.color == RED or robot.robot2:
            pass
        if robot.color == BLACK or robot.robot2:
            pass
        if robot.color == RED or robot.robot3:
            pass
        if robot.color == BLACK or robot.robot3:
            pass
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.grid[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
                left = -1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                        moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                        moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves
