from collections import deque
input = __import__('sys').stdin.readline

n, k = map(int, input().split())
q = deque([(n, 0)])
dist = [float('inf')] * 100001
dist[n] = 0
oob = lambda x: x < 0 or x > 100000
while q:
    x, ans = q.popleft()
    if x == k:
        print(dist[k])
        break
    for nx in x - 1, x + 1:
        if oob(nx) or ans + 1 >= dist[nx]:
            continue
        dist[nx] = ans + 1
        q.append((nx, ans + 1))
    if oob(x * 2) or ans >= dist[x * 2]:
        continue
    dist[x * 2] = ans
    q.append((x * 2, ans))