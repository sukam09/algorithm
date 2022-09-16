import math

def solution(n):
    root = math.sqrt(n)
    return int((root + 1) ** 2) if root == int(root) else -1