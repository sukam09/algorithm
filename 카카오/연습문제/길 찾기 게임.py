import sys
sys.setrecursionlimit(10000)

class Node:
    def __init__(self, val, x):
        self.val = val
        self.x = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self, node):
        self.root = node
        self.preorder = []
        self.postorder = []

    def insert(self, node):
        cur = self.root
        while True:
            if node.x < cur.x:
                if cur.left is not None:
                    cur = cur.left
                else:
                    cur.left = node
                    return
            else:
                if cur.right is not None:
                    cur = cur.right
                else:
                    cur.right = node
                    return

    def pretrv(self, node):
        self.preorder.append(node.val)
        if node.left is not None:
            self.pretrv(node.left)
        if node.right is not None:
            self.pretrv(node.right)

    def posttrv(self, node):
        if node.left is not None:
            self.posttrv(node.left)
        if node.right is not None:
            self.posttrv(node.right)
        self.postorder.append(node.val)

def solution(nodeinfo):
    n = len(nodeinfo)
    for i in range(n):
        nodeinfo[i] = [i + 1] + nodeinfo[i]
    
    nodeinfo.sort(key=lambda x: (-x[2], x[1]))
    root = Node(nodeinfo[0][0], nodeinfo[0][1])
    tree = Tree(root)
    
    for i in range(1, n):
        node = Node(nodeinfo[i][0], nodeinfo[i][1])
        tree.insert(node)
    
    tree.pretrv(root)
    tree.posttrv(root)

    return [tree.preorder, tree.postorder]