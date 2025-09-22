import pygame
import sys
from game import (
    new_grid, add_new_tile,
    move_left, move_right, move_up, move_down,
    can_move, SIZE
)

# --- Colors ---
BACKGROUND_COLOR = (187, 173, 160)
EMPTY_TILE_COLOR = (205, 193, 180)
TILE_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

FONT_COLOR = (119, 110, 101)
SCORE_COLOR = (255, 255, 255)

# --- Tile and window sizes ---
TILE_SIZE = 100
MARGIN = 10
WIDTH = HEIGHT = SIZE * (TILE_SIZE + MARGIN) + MARGIN

# --- Init Pygame ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + 60))
pygame.display.set_caption("2048 in Python (Pygame)")
font = pygame.font.SysFont("arial", 36, bold=True)
score_font = pygame.font.SysFont("arial", 28, bold=True)


def draw_grid(grid, score):
    """Draw the entire grid + score."""
    screen.fill(BACKGROUND_COLOR)

    # Draw score
    score_text = score_font.render(f"Score: {score}", True, SCORE_COLOR)
    screen.blit(score_text, (10, HEIGHT + 10))

    # Draw tiles
    for r in range(SIZE):
        for c in range(SIZE):
            value = grid[r][c]
            rect = pygame.Rect(
                c * (TILE_SIZE + MARGIN) + MARGIN,
                r * (TILE_SIZE + MARGIN) + MARGIN,
                TILE_SIZE,
                TILE_SIZE
            )
            color = TILE_COLORS.get(value, EMPTY_TILE_COLOR)
            pygame.draw.rect(screen, color, rect, border_radius=8)
            if value:
                text = font.render(str(value), True, FONT_COLOR)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

    pygame.display.flip()


def main():
    grid = new_grid()
    score = 0
    running = True

    while running:
        draw_grid(grid, score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                moved = False
                if event.key == pygame.K_LEFT:
                    grid, moved, gained = move_left(grid)
                elif event.key == pygame.K_RIGHT:
                    grid, moved, gained = move_right(grid)
                elif event.key == pygame.K_UP:
                    grid, moved, gained = move_up(grid)
                elif event.key == pygame.K_DOWN:
                    grid, moved, gained = move_down(grid)
                else:
                    continue

                if moved:
                    score += gained
                    add_new_tile(grid)

                if not can_move(grid):
                    print("Game Over! Final score:", score)
                    running = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
