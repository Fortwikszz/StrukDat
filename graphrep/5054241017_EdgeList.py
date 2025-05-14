def add_edge(edg, i, j):
    edg.append([i, j])

def display_adj_list(edg):
    for i in range(len(edg)):
        print(f"{i}: {edg[i]}")

V = 7
edg = []

add_edge(edg, 0, 1)
add_edge(edg, 0, 2)
add_edge(edg, 1, 2)
add_edge(edg, 1, 3)
add_edge(edg, 2, 4)
add_edge(edg, 3, 4)
add_edge(edg, 4, 5)
add_edge(edg, 5, 6)

print("Edge List Representation:")
display_adj_list(edg)