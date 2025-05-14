def add_edge(adj, i, j):
    adj[i].append(j)
    adj[j].append(i)

def display_adj_list(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end="")
        for j in adj[i]:
            print(j, end=" ")
        print()

V = 7
adj = [[] * V for _ in range(V)]  

add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 1, 2)
add_edge(adj, 1, 3)
add_edge(adj, 2, 4)
add_edge(adj, 3, 4)
add_edge(adj, 4, 5)
add_edge(adj, 5, 6)

print("Adjacency List Representation:")
display_adj_list(adj)