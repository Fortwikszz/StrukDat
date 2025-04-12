n = list(str(input()).strip())
stk = []
qyu = []
tempstr = ""
state = 0

for i in range(len(n)):
    if n[i].isalpha() or n[i] == "_":
        tempstr += n[i]
    elif n[i] == "[" or n[i] == "]":
        if state == 0:
            qyu.append(tempstr)
            tempstr = ""
        elif state == 1:
            stk.append(tempstr)
            tempstr = ""
        if n[i] == "[":
            state = 1
        elif n[i] == "]":
            state = 0

    print(tempstr)

if state == 0:
    qyu.append(tempstr)
elif state == 1:
    stk.append(tempstr)

for i in range(len(stk)):
    print(stk.pop(-1),end="")
for i in range(len(qyu)):
    print(qyu.pop(0),end="")

# print(stk)
# print(qyu)
# print(tempstr)