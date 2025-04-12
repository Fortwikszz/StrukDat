n = str(input())
parent = []
valid = 0

pair = {"(":")",
        "[":"]",
        "{":"}"}

open = ["(","[","{"]

for i in range(len(n)):
    if n[i] in open:
        parent.append(n[i])
    else:
        if len(parent) == 0:
            valid = 0
            break
        elif pair[parent[-1]] == n[i]:
            parent.pop()
        else:
            valid = 0
            break

    if len(parent) == 0 and i == len(n)-1:
        valid = 1

if valid == 0:
    print("NO")
else:
    print("YES")