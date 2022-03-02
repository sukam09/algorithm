input = __import__('sys').stdin.readline
from collections import deque
T = int(input())

for _ in range(T):
    func = input().strip()
    n = int(input())
    seq = input().strip()
    if seq != '[]':
        seq = seq[1:len(seq) - 1].split(',')
        seq = deque(map(int, seq))
    else: seq = deque()
    error = False
    r = 1
    for f in func:
        if f == 'R':
            r *= -1
        else:
            try: seq.popleft() if r == 1 else seq.pop()
            except:
                error = True
                break
    if error: print("error")
    else:
        seq = list(seq)
        if r == -1: seq = seq[::-1]
        print("[" + ','.join(list(map(str, list(seq)))) + "]")