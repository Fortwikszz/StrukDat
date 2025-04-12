from collections import deque

print("q for queue, s for stack")
p = str(input())
n = int(input())

if p == "q":
    queue = deque()

    for i in range(n):
        x = str(input())

        if x[0] == "+":
            queue.append(x[1:])
            print(queue)

        elif x[0] == "-":
            if len(queue) == 0:
                print("queue kosong lek")
            else:
                queue.popleft(queue)
                print(queue)

elif p == "s":
    stack = []

    for i in range(n):
        x = str(input())

        if x[0] == "+":
            stack.append(x[1:])
            print(stack)

        elif x[0] == "-":
            if len(stack) == 0:
                print("stack kosong lek")
            else:
                stack.pop()
                print(stack)