import numpy as np
import tkinter as tk

def load_maze_from_file(filename):
    return np.loadtxt(filename, dtype=int)

def render_maze(maze):
    cell_size = 5
    width = len(maze[0]) * cell_size
    height = len(maze) * cell_size
    
    root = tk.Tk()
    root.title("Maze Generator")
    
    canvas = tk.Canvas(root, width=width, height=height, bg="white")
    canvas.pack()
    
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            # color = "black" if maze[y][x] == 1 else "white"
            if maze[y][x] == 1:
                color = "black"
            elif maze[y][x] == 0:
                color = "white"
            elif maze[y][x] == 2:
                color = "green"
            elif maze[y][x] == 3:
                color = "red"
            canvas.create_rectangle(
                x * cell_size, y * cell_size,
                (x + 1) * cell_size, (y + 1) * cell_size,
                fill=color, outline=color
            )
    
    root.mainloop()

if __name__ == "__main__":
    maze = load_maze_from_file("maze.txt")
    render_maze(maze)