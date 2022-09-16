from sys import stdin
from collections import deque
input = stdin.readline

def sol(p, X):
    inv = False
    s = ''
    for x in X:
        if x != '[' and x != ']':
            s += x
    if s:
        s = s.split(',')
    else:
        s = []
    d = deque(s)
    for op in p:
        if op == 'R':
            inv = not inv
        else:
            if not d:
                return 'error', inv
            d.popleft() if not inv else d.pop()
    return d, inv

t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    X = input().rstrip()
    d, inv = sol(p, X)
    if d == 'error':
        print("error")
    else:
        if inv:
            d = reversed(d)
        print('[' + ','.join(d) + ']')