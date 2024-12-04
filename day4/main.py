import re
import numpy as np


file_path = "input1.txt"

grid = []
with open(file_path, 'r') as file:
    for line in file:
        grid.append(list(line.strip()))

grid = np.array(grid)

def horizontal (grid, word):
    reversedWord = word[::-1]
    result = 0;
    for row in grid:
        result += ''.join(row).count(word)
        result += ''.join(row).count(reversedWord)
    return result

def vertical (grid, word):
    reversedWord = word[::-1]
    result = 0;
    for column in grid.T:
        result += ''.join(column).count(word)
        result += ''.join(column).count(reversedWord)
    return result

def diagonal (grid, word):
    result = 0
    n_rows, n_cols = grid.shape

    diagonals = []
    for offset in range(-n_rows + 1, n_cols):
        diag = grid.diagonal(offset)
        diagonals.append(''.join(diag))

    anti_diagonals = []
    flipped = np.fliplr(grid)
    for offset in range(-n_rows + 1, n_cols):
        anti_diag = flipped.diagonal(offset)
        anti_diagonals.append(''.join(anti_diag))

    reversedWord = word[::-1]
    for diag in diagonals + anti_diagonals:
        result += diag.count(word)
        result += diag.count(reversedWord)

    return result

grid = np.array(grid)
word = 'XMAS'
print (horizontal (grid, word) + vertical (grid, word) + diagonal (grid, word))

search = np.array([
    ['M', '*', 'S'],
    ['*', 'A', '*'],
    ['M', '*', 'S'],
])

def generate_orientations(pattern):
    orientations = []
    orientations.append(pattern)
    for k in [1, 2, 3]:
        orientations.append(np.rot90(pattern, k))
    return orientations

def matches_pattern(grid_section, pattern):
    grid_flat = grid_section.flatten()
    pattern_flat = pattern.flatten()
    for g_char, p_char in zip(grid_flat, pattern_flat):
        if p_char != '*' and g_char != p_char:
            return False
    return True


def count_pattern_occurrences(grid, pattern):
    count = 0
    grid_size = grid.shape[0]
    orientations = generate_orientations(pattern)
    pattern_size = pattern.shape[0]

    for orient in orientations:
        for i in range(grid_size - pattern_size + 1):
            for j in range(grid_size - pattern_size + 1):
                grid_section = grid[i:i + pattern_size, j:j + pattern_size]
                if matches_pattern(grid_section, orient):
                    count += 1
    return count

print (count_pattern_occurrences(grid, search))