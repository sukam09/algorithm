import sys
from itertools import combinations
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())
ii = lambda: int(input())

def solve(c):
    global ans
    x, y = c[0]
    vis = [[0] * 5 for _ in range(5)]
    vis[x][y] = 1
    q = deque([(x, y)])
    cnt = {'S': 0, 'Y': 0}
    cnt[board[x][y]] += 1
    while q:
        x, y = q.popleft()
        if cnt['S'] + cnt['Y'] == 7 and cnt['S'] >= 4:
            ans += 1
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if oob(nx, ny) or vis[nx][ny] or (nx, ny) not in c:
                continue
            vis[nx][ny] = 1
            q.append((nx, ny))
            cnt[board[nx][ny]] += 1

board = [input() for _ in range(5)]
cand = [(i, j) for i in range(5) for j in range(5)]
ans = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
oob = lambda x, y: x < 0 or x >= 5 or y < 0 or y >= 5
for c in combinations(cand, 7):
    solve(c)
print(ans)