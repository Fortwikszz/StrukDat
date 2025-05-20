class tree:
    def __init__(self, key = None, lvl = 0):
        self.key = key
        self.items = []
        self.level = lvl

    def cangkok(self, y):
        self.items.appedn(y)

    def potong(self, x):
        self.key = None

n = int(input())
m = list(map(int, input().split()))
x = int(input())
phn = tree()

for i in range(x):
    a = list(map(str, input().split()))
    if a[0] == "cangkok":
        if phn.key == None:
            phn.key = a[1]
            phn.items.append(a[2])
        else:
            if 
        