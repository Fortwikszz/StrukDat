def add_edge(mat, i, j):
    mat[i][j] = 1
    mat[j][i] = 1

def display_matrix(mat):
    for row in mat:
        print(" ".join(map(str, row)))  

V = 7
mat = [[0] * V for _ in range(V)]  

add_edge(mat, 0, 1)
add_edge(mat, 0, 2)
add_edge(mat, 1, 2)
add_edge(mat, 1, 3)
add_edge(mat, 2, 4)
add_edge(mat, 3, 4)
add_edge(mat, 4, 5)
add_edge(mat, 5, 6)

print("Adjacency Matrix:")
display_matrix(mat)