import pygame
import sys

# Initialize pygame
pygame.init()

# Grid settings
GRID_SIZE = 5
CELL_SIZE = 100
WIDTH = HEIGHT = GRID_SIZE * CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("5x5 Grid Game")

# Grid data
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


def draw_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect((col * CELL_SIZE), (row * CELL_SIZE), CELL_SIZE, CELL_SIZE)

            if grid[row][col] == 1:
                for _ in range(GRID_SIZE*GRID_SIZE):

                    pygame.draw.rect(screen, BLACK, _)

            pygame.draw.rect(screen, BLACK, rect, 2)  # border


def handle_click(pos):
    x, y = pos
    col = x // CELL_SIZE
    row = y // CELL_SIZE

    # Toggle cell
    grid[row][col] = 1 if grid[row][col] == 0 else 0


# Main loop
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_click(pygame.mouse.get_pos())

    draw_grid()
    pygame.display.flip()