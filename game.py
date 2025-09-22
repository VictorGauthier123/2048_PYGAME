import random

SIZE = 4


def new_grid():
    """Créer une nouvelle grille avec deux cases remplies (2 ou 4)."""
    grid = [[0] * SIZE for _ in range(SIZE)]
    add_new_tile(grid)
    add_new_tile(grid)
    return grid


def add_new_tile(grid):
    """Ajoute un nouveau 2 (90%) ou 4 (10%) dans une case vide."""
    empty = [(r, c) for r in range(SIZE) for c in range(SIZE) if grid[r][c] == 0]
    if empty:
        r, c = random.choice(empty)
        grid[r][c] = random.choices([2, 4], [0.9, 0.1])[0]


def compress(row):
    """Décale tous les nombres d'une ligne vers la gauche (supprime les zéros au milieu)."""
    new_row = [num for num in row if num != 0]
    new_row += [0] * (SIZE - len(new_row))
    return new_row


def merge(row):
    """Fusionne les nombres identiques côte à côte (une fois max)."""
    score = 0
    for i in range(SIZE - 1):
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            score += row[i]
            row[i + 1] = 0
    return row, score


def move_left(grid):
    changed = False
    score_gain = 0
    new_grid = []
    for row in grid:
        compressed = compress(row)
        merged, score = merge(compressed)
        compressed = compress(merged)
        new_grid.append(compressed)
        if compressed != row:
            changed = True
        score_gain += score
    return new_grid, changed, score_gain


def reverse(grid):
    return [row[::-1] for row in grid]


def transpose(grid):
    return [list(row) for row in zip(*grid)]


def move_right(grid):
    reversed_grid = reverse(grid)
    new_grid, changed, score = move_left(reversed_grid)
    return reverse(new_grid), changed, score


def move_up(grid):
    transposed = transpose(grid)
    new_grid, changed, score = move_left(transposed)
    return transpose(new_grid), changed, score


def move_down(grid):
    transposed = transpose(grid)
    new_grid, changed, score = move_right(transposed)
    return transpose(new_grid), changed, score


def can_move(grid):
    """Vérifie si des mouvements sont possibles."""
    # Case vide dispo
    for row in grid:
        if 0 in row:
            return True
    # Fusion possible horizontalement
    for r in range(SIZE):
        for c in range(SIZE - 1):
            if grid[r][c] == grid[r][c + 1]:
                return True
    # Fusion possible verticalement
    for r in range(SIZE - 1):
        for c in range(SIZE):
            if grid[r][c] == grid[r + 1][c]:
                return True
    return False
