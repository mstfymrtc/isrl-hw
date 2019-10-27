import pygame, sys


class Robot:
    score = 0

    def __init__(self, row, col):
        self.row = row
        self.col = col


# Define globals
TILESIZE = 40
MAPWIDTH = 12
MAPHEIGHT = 12
MARGIN = 0.99

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
       [N, N, W, F, N, N, N, F, F, W, N, N],
       [W, N, W, F, N, W, F, W, N, N, F, W]]

# Initialize robots
r1 = Robot(3, 4)
r2 = Robot(0, 1)

pygame.init()
DISPLAY = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))
DISPLAY.fill(WHITE)

while True:
    # print(f"r1-row: {r1.row} r1-col: {r1.col}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if r1.col != 0:
                if (event.key == pygame.K_LEFT) and (map[r1.row][r1.col - 1] != W):
                    r1.col -= 1

            if r1.col != 11:
                if (event.key == pygame.K_RIGHT) and (map[r1.row][r1.col + 1] != W):
                    r1.col += 1

            if r1.row != 0:
                if (event.key == pygame.K_UP) and (map[r1.row - 1][r1.col] != W):
                    r1.row -= 1

            if r1.row != 11:
                if (event.key == pygame.K_DOWN) and (map[r1.row + 1][r1.col] != W):
                    r1.row += 1

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
