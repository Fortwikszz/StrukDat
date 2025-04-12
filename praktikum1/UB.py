n = int(input())

barisan = list(map(int, input().split()))
res = []

for i in range(n):
    if i == 0:
        res.append(-1)
    else:
        tinggian = True
        for j in range(i,-1,-1):
            if barisan[i] < barisan[j]:
                res.append(j)
                tinggian = False
                break
        if tinggian:
            res.append(-1)

for i in range(len(res)):
    print(res[i], end=' ')