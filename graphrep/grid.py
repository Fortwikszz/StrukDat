import heapq

grid = [[0,2,4],[3,2,1],[1,0,4]]
if grid[0][1] > 1 and grid[1][0] > 1:
    print(-1)

def dijkstra(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    min_heap = [(grid[0][0], start)]
    
    while min_heap:
        cost, (x, y) = heapq.heappop(min_heap)
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        if (x, y) == goal:
            return cost
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                wait_time = 1 if (grid[nx][ny] - cost) % 2 == 0 else 0
                next_time = max(grid[nx][ny] + wait_time, cost + 1)
                heapq.heappush(min_heap, (next_time, (nx, ny)))
    
    return -1

start = (0, 0)
goal = (len(grid) - 1, len(grid[0]) - 1)
result = dijkstra(grid, start, goal)
print(result)