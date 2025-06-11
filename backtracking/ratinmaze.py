def is_safe(maze, x, y, n):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1

def solve_maze_util(maze, x, y, n, path, sol):
    if x == n - 1 and y == n - 1:
        sol.append(''.join(path))
        return

    for dx, dy, move in [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]:
        new_x, new_y = x + dx, y + dy
        if is_safe(maze, new_x, new_y, n):
            maze[x][y] = -1
            path.append(move)
            solve_maze_util(maze, new_x, new_y, n, path, sol)
            path.pop()
            maze[x][y] = 1

def solve_maze(maze):
    sol = []
    solve_maze_util(maze, 0, 0, len(maze), [], sol)
    return sol

if __name__ == "__main__":
    maze = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]
    print(solve_maze(maze))
