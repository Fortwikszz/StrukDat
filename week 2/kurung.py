n = str(input())
parent = []

pair = {"(":")",
        "[":"]",
        "{":"}"}

open = ["(","[","{"]

for i in range(len(n)):
    if n[i] in open:
        parent.append(n[i])
    else:
        if len(parent) == 0:
            print("NO")
            break
        elif pair[parent[-1]] == n[i]:
            parent.pop()
        else:
            print("NO")
            break

if len(parent) == 0:
    print("YES")