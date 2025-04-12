n = int(input())
main = []
min = []

for i in range(n):
    x = list(input().split(" "))

    if x[0] == "push":
        if len(main) == 0:
            min.append(x[1])
            main.append(x[1])
        else:
            main.append(x[1])
            if int(x[1]) < int(min[-1]):
                min.append(x[1])
    elif x[0] == "pop":
        if main[-1] == min[-1]:
            min.pop()
        main.pop()
    elif x[0] == "min":
        print(min[-1])

    # print(main)
    # print(min)

# print(main)
# print(min)