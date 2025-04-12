n, x = map(int, input().split())

plushies = list(map(int, input().split()))
depth = dict()
tree = dict()
# print(plushies)

for i in range(n-1):
    a = list(map(int, input().split()))
    depth2 = int()
    
    if a[0] not in tree:
        tree.update({a[0]: [a[1]]})
    else:
        tree[a[0]] += [a[1]]

    # if a[0] == 0:
    #     depth2 = 1
    # else:
    #     for j in depth:
    #         if a[0] in depth[j]:
    #             depth2 = j+1
    
    # if depth2 not in depth:
    #     depth.update({depth2: [a[1]]})
    # else:
    #     depth[depth2] += [a[1]]

res = []
# reverse = False

# if x < sum(plushies):
#     reverse = True

# if reverse:
#     res.append(plushies[0])
#     for i in depth:
#         for j in range(len(depth[i])-1, -1, -1):
#             res.append(plushies[depth[i][j]])
# else:
#     res.append(plushies[0])
#     for i in depth:
#         for j in range(len(depth[i])):
#             res.append(plushies[depth[i][j]])


# for i in range(len(res)):
#     print(res[i], end=' ')

# print()
# print(tree)
# print(depth)

nodesum = []
for i in range(len(plushies)):
    tempres = 0
    q = [i]
    while len(q) != 0:
        if q[0] in tree:
            q += tree[q[0]]
        tempres += plushies[q[0]]
        q.pop(0)
    nodesum.append(tempres)

q = [0]
while len(q) != 0:
    if q[0] in tree:
        if nodesum[q[0]] > x:
            for i in range(len(tree[q[0]])-1, -1, -1):
                q.append(tree[q[0]][i])
        else:
            q += tree[q[0]]
    res += [plushies[q[0]]]
    q.pop(0)

for i in range(len(res)):
    print(res[i], end=' ')