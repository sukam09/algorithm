from collections import deque
input = __import__('sys').stdin.readline

f, s, g, u, d = map(int, input().split())
vis = [0] * 1000001
q = deque([(s, 0)])
vis[s] = 1
oob = lambda x: x < 1 or x > f
while q:
    x, ans = q.popleft()
    if x == g:
        print(ans)
        break
    for nx in x + u, x - d:
        if oob(nx) or vis[nx]:
            continue
        vis[nx] = 1
        q.append((nx, ans + 1))
else:
    print("use the stairs")