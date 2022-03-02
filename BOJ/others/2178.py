from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]
q = deque([(0, 0)])
ans = [[0] * M for _ in range(N)]
ans[0][0] = 1
while q:
    x, y = q.popleft()
    if x == N - 1 and y == M - 1:
        print(ans[x][y])
    cur = ans[x][y]
    if x + 1 < N and maze[x + 1][y] and not ans[x + 1][y]:
        q.append((x + 1, y))
        ans[x + 1][y] = cur + 1
    if y + 1 < M and maze[x][y + 1] and not ans[x][y + 1]:
        q.append((x, y + 1))
        ans[x][y + 1] = cur + 1
    if x - 1 >= 0 and maze[x - 1][y] and not ans[x - 1][y]:
        q.append((x - 1, y))
        ans[x - 1][y] = cur + 1
    if y - 1 >= 0 and maze[x][y - 1] and not ans[x][y - 1]:
        q.append((x, y - 1))
        ans[x][y - 1] = cur + 1