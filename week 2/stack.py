n = int(input())
stack = []

for i in range(n):
    x = str(input())

    if x[0] == "+":
        stack.append(x[1:])
        print(len(stack))

    elif x[0] == "-":
        print(stack[-1],end=";")
        stack.pop()
        print(stack)