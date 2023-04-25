import sys
import math

M, N = map(int, sys.stdin.readline().split())

# 에라토스테네스의 체 이용해서 풀어보기
e = {x: 1 for x in range(2, N + 1)}
prime = []

while True:
    p = list(e.keys())[0]
    prime.append(p)
    del e[p]
    if p <= math.sqrt(N):
        keys = list(e.keys())
        for key in keys:
            if key % p == 0:
                del e[key]
    else:
        prime.extend([x for x in e])
        break

ans = [str(x) for x in prime if x >= M]
print('\n'.join(ans))
