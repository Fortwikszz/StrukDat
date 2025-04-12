num = int(input())
stk = []
res = []
finres = []

op = ["+","-","*","/","^"]

for _ in range(num):
    n = list(str(input().strip()))
    for i in n:
        if i.isalpha():
            res.append(i)
        elif i in op:
            stk.append(i)
        elif i == ")":
            res.append(stk[-1])
            stk.pop()
    finres.append(res)
    res = []
    
        
for i in finres:
    for j in i:
        print(j,end="")
    print()