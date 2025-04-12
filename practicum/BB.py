n = int(input())

barisan = []
res = []
for i in range(n):
    barisan += [i+1]

for i in range(n):
    barisan.append(barisan[0])
    # print(barisan)
    barisan.pop(0)
    # print(barisan)

    res += [barisan[0]]
    barisan.pop(0)
    # print()

for i in res:
    print(i, end=' ')