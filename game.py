import pygame, sys
from random import randrange


class Robot:

    def __init__(self, row, col, name):
        self.row = row
        self.col = col
        self.name = name
        self.score = 0

    def increaseScore(self):
        self.score += 1

    def printScore(self):
        print(f"{self.name}'s score: {self.score}")


# Define globals
TILESIZE = 40
MAPWIDTH = 12
MAPHEIGHT = 12
MARGIN = 0.99
DELAY = 25

# Define tiles
N = 0  # nothing
W = 1  # wall
F = 2  # food

# Define colors
BLACK = (0, 0, 0)
BROWN = (160, 82, 45)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Map tiles with colors
TileColour = {
    N: BLACK,
    W: BROWN,
    F: YELLOW,
}

# Define map
map = [[N, W, N, W, W, F, N, W, W, N, W, W],
       [W, N, W, F, N, N, F, W, N, N, F, W],
       [N, N, F, N, W, N, W, W, F, F, W, W],
       [F, F, N, N, N, N, N, N, N, N, N, N],
       [W, N, W, N, N, N, W, N, N, F, W, N],
       [N, N, W, N, N, N, W, F, F, W, N, N],
       [W, N, W, N, N, N, F, W, N, N, F, W],
       [W, N, W, N, N, N, W, N, N, F, W, N],
       [F, F, N, N, N, F, N, N, N, N, N, N],
       [N, W, N, W, W, F, N, N, W, N, W, W],
       [N, N, W, F, N, N, N, F, F, N, N, N],
       [W, N, W, F, N, W, F, W, N, N, F, W]]

# Initialize robots
r1 = Robot(3, 4, "Robocop")
r2 = Robot(3, 4, "Babur")

pygame.init()
pygame.display.set_caption('2D Robot World')
DISPLAY = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))
DISPLAY.fill(WHITE)


# Define movement functions
def forward(robot):
    if robot.row != 0:
        if map[robot.row - 1][robot.col] != W:
            robot.row -= 1
            pygame.time.wait(DELAY)


def backward(robot):
    if robot.row != 11:
        if map[robot.row + 1][robot.col] != W:
            robot.row += 1
            pygame.time.wait(DELAY)


def left(robot):
    if robot.col != 0:
        if map[robot.row][robot.col - 1] != W:
            robot.col -= 1
            pygame.time.wait(DELAY)


def right(robot):
    if robot.col != 11:
        if map[robot.row][robot.col + 1] != W:
            robot.col += 1
            pygame.time.wait(DELAY)


while True:
    # print(f"r1-row: {r1.row} r1-col: {r1.col}")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ################################################# Plan for Robocop ################################################
    if r1.row != 0 and r1.row != 11 and r1.col != 0 and r1.col != 11:  # limits
        if (map[r1.row][r1.col + 1] != W) or (map[r1.row][r1.col - 1] != W) or (map[r1.row + 1][r1.col] != W) or (
                map[r1.row - 1][r1.col] != W):
            # If robot is not in the map's limit & there is no wall around, randomly pick a route to navigate
            num = randrange(0, 4)
            if num == 0:
                forward(r1)
            elif num == 1:
                backward(r1)
            elif num == 2:
                right(r1)
            else:
                left(r1)

    else:  # If a robot in the map's limit, then randomly pick a route to navigate
        num = randrange(0, 4)
        if num == 0:
            forward(r1)
        elif num == 1:
            backward(r1)
        elif num == 2:
            right(r1)
        else:
            left(r1)
    ##################################################################################################################

    # If cell contains food, delete it and increase robot's score
    if map[r1.row][r1.col] == F:
        map[r1.row][r1.col] = N
        r1.increaseScore()
        # r1.printScore()

    for row in range(MAPHEIGHT):
        for col in range(MAPWIDTH):
            pygame.draw.rect(DISPLAY, TileColour[map[row][col]],
                             (col * TILESIZE, row * TILESIZE, TILESIZE * MARGIN, TILESIZE * MARGIN))

    # DRAW ROBOT 1
    pygame.draw.rect(DISPLAY, RED,
                     (r1.col * TILESIZE, r1.row * TILESIZE, TILESIZE * MARGIN, TILESIZE * MARGIN))

    # DRAW ROBOT 2
    pygame.draw.rect(DISPLAY, BLUE,
                     (r2.col * TILESIZE, r2.row * TILESIZE, TILESIZE * MARGIN, TILESIZE * MARGIN))

    pygame.display.update()
