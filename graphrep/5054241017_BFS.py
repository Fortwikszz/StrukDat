from collections import deque

def bfs(adj):
    V = len(adj)
    res = []
    s = 0
    q = deque()
    visited = [False] * V
    
    visited[s] = True
    q.append(s)
    
    while q:  
        curr = q.popleft()
        res.append(curr)
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
                
    return res

adj = [[1, 2], [0, 2, 3], [0, 1, 4], [1, 4], [2, 3, 5], [4, 6], [5]]
ans = bfs(adj)
for i in ans:
    print(i, end=" ")