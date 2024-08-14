import numpy as np
import random

def generate_maze(width, height):
    # Initialize the grid with walls
    maze = np.ones((height, width), dtype=int)
    
    def carve_passages_from(start_x, start_y):
        stack = [(start_x, start_y)]
        maze[start_y][start_x] = 0
        
        while stack:
            cx, cy = stack[-1]
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(directions)
            carved = False
            
            for direction in directions:
                nx, ny = cx + direction[0] * 2, cy + direction[1] * 2
                if 1 <= nx < width - 1 and 1 <= ny < height - 1 and maze[ny][nx] == 1:
                    maze[cy + direction[1]][cx + direction[0]] = 0
                    maze[ny][nx] = 0
                    stack.append((nx, ny))
                    carved = True
                    break
            
            if not carved:
                stack.pop()
    
    start_x, start_y = width - 2, 1  # Start just inside the top right corner
    carve_passages_from(start_x, start_y)
    
    return maze

def save_maze_to_file(maze, filename):
    np.savetxt(filename, maze, fmt='%d')

if __name__ == "__main__":
    width, height = 102, 102  # Add 2 to width and height for the outer walls
    maze = generate_maze(width, height)
    save_maze_to_file(maze, "maze.txt")