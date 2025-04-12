n = int(input())

enemy = list(map(int, input().split()))
res = []

for i in range(n):
    stronger = True
    for j in range(i+1, n):
        if enemy[j] > enemy[i]:
            res.append(j-i)
            stronger = False
            break
    if stronger:
        res.append(0)

for i in range(len(res)):
    print(res[i], end=' ')