import sys
from collections import deque

sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

x, y = map(int, input().split())
maze = []
for _ in range(x):
    maze.append(list(input().strip()))

start = None
goal = None
for i in range(x):
    for j in range(y):
        if maze[i][j] == "A":
            start = (i, j)
        if maze[i][j] == "B":
            goal = (i, j)

def bfs(maze, start, goal, x, y):
    if start == goal:
        return []
    start_idx = start[0] * y + start[1]
    goal_idx = goal[0] * y + goal[1]
    
    queue = deque()
    queue.append(start)
    visited = [False] * (x * y)
    prev = [-1] * (x * y)  # Use -1 to indicate no previous
    move_from = [None] * (x * y)
    visited[start[0] * y + start[1]] = True
    
    directions = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]
    
    found = False
    while queue:
        cx, cy = queue.popleft()
        current_idx = cx * y + cy
        if (cx, cy) == goal:
            found = True
            break
        for dx, dy, move in directions:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < x and 0 <= ny < y and maze[nx][ny] != '#':
                idx = nx * y + ny
                if not visited[idx]:
                    visited[idx] = True
                    prev[idx] = current_idx
                    move_from[idx] = move
                    if (nx, ny) == goal:
                        # Early termination: clear queue and add goal to process next
                        queue.clear()
                        queue.append((nx, ny))
                        found = True
                        break  # break out of directions loop
                    queue.append((nx, ny))
        if found:
            break  # break out of while loop if goal found in directions
    
    if not found:
        return None
    
    # Reconstruct path
    path = []
    current = goal_idx
    while current != start_idx:
        move = move_from[current]
        if move is None:
            return None  # This should not happen if path exists
        path.append(move)
        current = prev[current]
    path.reverse()
    return path

res = bfs(maze, start, goal, x, y)
if res is not None:
    print("YES")
    print(len(res))
    print("".join(res))
else:
    print("NO")