# Make a 100x100 grid of 0s

import numpy as np

grid = np.zeros((100, 100), dtype=int)
np.savetxt('grid.txt', grid, fmt='%d', delimiter=' ')


def make_path_ways(grid_file):
    # Read the grid file
    grid = np.loadtxt(grid_file, dtype=int, delimiter=' ')

    # Replace random 0s with 2s (pathways) in the grid
    for i in range(100):
        for j in range(100):
            if np.random.randint(0, 100) < 10:
                grid[i, j] = 2

    # Link every 2s with 1s (one way)
    for i in range(100):
        for j in range(100):
            if grid[i, j] == 2:
                if i-1 >= 0 and grid[i-1, j] == 0:
                    grid[i-1, j] = 1
                if i+1 < 100 and grid[i+1, j] == 0:
                    grid[i+1, j] = 1
                if j-1 >= 0 and grid[i, j-1] == 0:
                    grid[i, j-1] = 1
                if j+1 < 100 and grid[i, j+1] == 0:
                    grid[i, j+1] = 1

    # Replace 2s with 1s in the grid
    for i in range(100):
        for j in range(100):
            if grid[i, j] == 2:
                grid[i, j] = 1

    # Save the grid with pathways
    np.savetxt('grid_with_pathways.txt', grid, fmt='%d', delimiter=' ')


def bautify_maze(grid_file):
    # Read the grid file
    grid = np.loadtxt(grid_file, dtype=int, delimiter=' ')

    # 0 = empty, 1 = wall, 2 = pathway
    # 0 = 🟢 
    # 1 = 🔴
    # 2 = 🟡

    # Print maze but with characters
    for i in range(100):
        for j in range(100):
            if grid[i, j] == 0:
                print('🟢', end=' ')
            elif grid[i, j] == 1:
                print('🔴', end=' ')
            else:
                print('🟡', end=' ')
        print()



make_path_ways('grid.txt')
bautify_maze('grid_with_pathways.txt')