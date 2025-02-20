import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 60
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Candy colors
CANDY_COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE]

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Candy Crush")

# Clock
clock = pygame.time.Clock()

# Grid
grid = [[random.choice(CANDY_COLORS) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(screen, grid[y][x], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def swap_candies(x1, y1, x2, y2):
    grid[y1][x1], grid[y2][x2] = grid[y2][x2], grid[y1][x1]

def find_matches():
    matches = []
    # Check horizontal matches
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH - 2):
            if grid[y][x] == grid[y][x + 1] == grid[y][x + 2]:
                matches.append((x, y))
                matches.append((x + 1, y))
                matches.append((x + 2, y))
    # Check vertical matches
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT - 2):
            if grid[y][x] == grid[y + 1][x] == grid[y + 2][x]:
                matches.append((x, y))
                matches.append((x, y + 1))
                matches.append((x, y + 2))
    return matches

def remove_matches(matches):
    for x, y in matches:
        grid[y][x] = None

def fill_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x] is None:
                grid[y][x] = random.choice(CANDY_COLORS)

def main():
    running = True
    selected = None
    while running:
        screen.fill(WHITE)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                grid_x, grid_y = x // CELL_SIZE, y // CELL_SIZE
                if selected is None:
                    selected = (grid_x, grid_y)
                else:
                    swap_candies(selected[0], selected[1], grid_x, grid_y)
                    matches = find_matches()
                    if matches:
                        remove_matches(matches)
                        fill_grid()
                    selected = None

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()