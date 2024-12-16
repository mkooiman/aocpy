import numpy as np

file_path = ("input1.txt")

grid = []
with open(file_path, 'r') as file:
    for line in file:
        grid.append(list(line.strip()))
npGrid = np.array(grid)

playerChar = '^'
walkedPosition = 'X'
wall = '#'
found = True

def map_coordinates(row, col, rows, columns):
    new_row = columns - 1 - col
    new_col = row
    return new_row, new_col

np.set_printoptions(precision=0, suppress=True, threshold=np.inf, linewidth=np.inf)

def walk(grid):
    visited_states = []
    currentPosition = np.argwhere(grid == playerChar)
    if currentPosition.size == 0:
        return grid, False, False

    rotation_count = 0
    while True:
        playerRow, playerCol = currentPosition[0]
        found = False
        for row in range(playerRow, -1, -1):
            if grid[row, playerCol] == wall:
                grid[min(playerRow, row)+1:max(playerRow, row), playerCol] = walkedPosition
                grid = np.rot90(grid)
                rotation_count = (rotation_count + 1 ) % 4
                currentPosition = [map_coordinates(row+1, playerCol, grid.shape[0], grid.shape[1])]
                found = True

                state_tuple = (min(playerRow, row)+1, max(playerRow, row), playerCol, rotation_count)


                if state_tuple in visited_states:
                    return grid, False, True
                    while rotation_count != 0:
                        grid = np.rot90(grid)
                        rotation_count = (rotation_count + 1 ) % 4
                else:
                    visited_states.append(state_tuple)
                break

        if not found:
            grid[0:playerRow, playerCol] = walkedPosition
            while rotation_count != 0:
                grid = np.rot90(grid)
                rotation_count = (rotation_count + 1) % 4
            return grid, False, False
    return grid, found, looped

newGrid, found, looped = walk(np.copy(npGrid))

print('Answer 1: ' + str(np.count_nonzero(newGrid == 'X')))
x_positions = np.argwhere(newGrid == 'X')
positions = 0
for r, c in x_positions:
    tmpGrid = np.copy(npGrid)
    tmpGrid[r, c] = wall
    _, _, loopedResult = walk(tmpGrid)
    if(loopedResult):
        positions += 1

print('Answer 2: ' + str(positions))
