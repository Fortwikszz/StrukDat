line = [2, 4, 3, 6, 3, 7, 1]
res = []
tree = dict()
tree.update({0: [1, 2, 3],
             1: [4],
             3: [5, 6]})

for i in range(len(line)):
    tempres = 0
    q = [i]
    while len(q) != 0:
        if q[0] in tree:
            q += tree[q[0]]
        tempres += line[q[0]]
        q.pop(0)
    res.append(tempres)

print(res)