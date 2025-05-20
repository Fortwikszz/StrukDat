class node:
    def __init__(self, key = None):
        self.key = key
        self.right = None
        self.left = None

    def num(self):
        return int(self.key)
    
tree = node()

n, s = map(int, input().split())

for i in range(n):
    x = int(input())
    if tree.key == None:
        tree.key = x
    else:
        current = tree
        while True:
            if x < current.num():
                if current.left:
                    current = current.left
                else:
                    current.left = node(x)
                    # print(current.num())
                    break

            elif x >= current.num():
                if current.right:
                    current = current.right
                else:
                    current.right = node(x)
                    # print(current.num())
                    break

tot = [0]
prlvl = [[None]]*10
def rec(treee, lvl):
    if treee.left:
        rec(treee.left, lvl+1)
    tot[0] += treee.num()
    if treee.right:
        rec(treee.right, lvl+1)
rec(tree, 0)

# print(prlvl)
# print(tot)

if tot[0] <= s:
    print("Yeyy")
else:
    print("Bleh")