import heapq
import sys

def constructAdj(edges, V):
    adj = [[] for _ in range(V)]

    for edge in edges:
        u, v, wt = edge
        adj[u].append([v, wt])
        adj[v].append([u, wt])

    return adj

def dijkstra(V, edges, src):
    adj = constructAdj(edges, V)
    pq = []
    dist = [sys.maxsize] * V

    heapq.heappush(pq, [0, src])
    dist[src] = 0

    while pq:
        u = heapq.heappop(pq)[1]

        for x in adj[u]:
            v, weight = x[0], x[1]

            if dist[v] > dist[u] + weight:
                snode[v] = u
                dist[v] = dist[u] + weight
                heapq.heappush(pq, [dist[v], v])

    return dist

def displayres(result, snode):
    for i in range(len(result)):
        temp = i
        stk = [i]
        print(f"Node {i}: {result[i]} | ", end="")
        while snode[temp] != 0:
            stk.append(snode[temp])
            temp = snode[temp]
        stk.append(0)
        for j in range(len(stk) - 1, -1, -1):
            if j == 0:
                print(stk[j], end="")
            else:
                print(stk[j], end=" -> ")
        print()

V = 9
src = 0
snode = [0 for _ in range(V)]

edges = [[0, 1, 4],
         [0, 7, 8],
         [1, 7, 11],
         [1, 2, 8],
         [2, 3, 7],
         [2, 5, 4],
         [2, 8, 2],
         [3, 4, 9],
         [3, 5, 14],
         [4, 5, 10],
         [5, 6, 2],
         [6, 7, 1],
         [7, 8, 7]]

result = dijkstra(V, edges, src)

displayres(result, snode)