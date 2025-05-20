class node:
    def __init__(self, key = None):
        self.key = key
        self.right = None
        self.left = None

    def num(self):
        return int(self.key)

tree = node()
n = list(map(int, input().split()))

for i in range(len(n)):
    if tree.key == None:
        tree.key = n[i]
    else:
        current = tree
        while True:
            if n[i] < current.num():
                if current.left:
                    current = current.left
                else:
                    current.left = node(n[i])
                    # print(current.num())
                    break

            elif n[i] >= current.num():
                if current.right:
                    current = current.right
                else:
                    current.right = node(n[i])
                    # print(current.num())
                    break

temp = []
res = []
def recurse(treee, way = None, get = []):
    if not treee.right and not treee.left and way == "right":
        get.append(treee.num())
        for i in get:
            print(i, end="")
    if treee.right:
        get.append(treee.num())
        recurse(treee.right, "right", get)
    if treee.left:
        get.append(treee.num())
        recurse(treee.left, "left", get)

recurse(tree)