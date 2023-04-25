from collections import Counter
input = __import__('sys').stdin.readline
N = int(input())
L = [input().strip() for _ in range(N)]
C = Counter(L)
MC = [c for c in C.items() if c[1] == max(C.values())]
if len(MC) == 1: print(MC[0][0])
else: MC = sorted(MC, key=lambda x: x[0]); print(MC[0][0])