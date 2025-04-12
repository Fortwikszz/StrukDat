def initree(tree, key):
    tree = {"key": key, "left" : None, "right" : None}

def addtree(tree, key):
    if tree == None:
        tree = {"key" : key, "left" : None, "right" : None}