import heapq

grid = [[0,2,4],[3,2,1],[1,0,4]]

def dijkstra(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    min_heap = [(0, start)]
    
    while min_heap:
        cost, (x, y) = heapq.heappop(min_heap)
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        if (x, y) == goal:
            return cost
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] <= cost + 1:
                heapq.heappush(min_heap, (1 + cost, (nx, ny)))
    
    return -1

start = (0, 0)
goal = (len(grid) - 1, len(grid[0]) - 1)
result = dijkstra(grid, start, goal)
print(result)