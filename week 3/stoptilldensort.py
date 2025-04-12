n, stop = map(int, input().split())
x = []
stak1 = []
stak2 = []

for i in range(n):
    x.append(int(input()))

for i in range(len(x)):
    if i == stop:
        break
    elif i == 0:
        stak1.append(x[i])
    else:
        if stak1[-1] <= x[i]:
            stak1.append(x[i])

            print(stak1)
            print(stak2)
            print()

        else:
            while stak1[-1] > x[i]:
                stak2.append(stak1[-1])
                stak1.pop()

                print(stak1)
                print(stak2)
                print()

                if len(stak1) == 0:
                    break

            stak1.append(x[i])

            print(stak1)
            print(stak2)
            print()

            while stak2:
                stak1.append(stak2[-1])
                stak2.pop()

                print(stak1)
                print(stak2)
                print()

print(stak1)