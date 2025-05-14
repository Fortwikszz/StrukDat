def dfsRec(adj, visited, s, res):
    visited[s] = True
    res.append(s)

    for i in range(len(adj)):
        if adj[s][i] == 1 and not visited[i]:
            dfsRec(adj, visited, i, res)


def DFS(adj):
    visited = [False] * len(adj)
    res = []
    dfsRec(adj, visited, 0, res)
    return res


def add_edge(adj, s, t):
    adj[s][t] = 1
    adj[t][s] = 1

V = 7
adj = [[0] * V for _ in range(V)]

edges = [(0,1), (0,2), (1,2), (1,3), (2,4), (3,4), (4,5), (5,6)]

for s, t in edges:
    add_edge(adj, s, t)

res = DFS(adj)
print(" ".join(map(str, res)))