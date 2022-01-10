from sys import stdin
from itertools import combinations
from collections import deque
input = stdin.readline

def bfs(r, c, nb):
    vis = [[0] * m for _ in range(len(nb))]
    q = deque([(r, c, 0)])
    vis[r][c] = 1
    res = []
    
    # 탐색할 때 궁수든 적이든 빈 칸이든 모두 탐색을 해야 함
    while q:
        x, y, dist = q.popleft()
        if nb[x][y] == 1 and 1 <= dist <= d:
            res.append((x, y, dist))
        for nx, ny in (x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y):
            if 0 <= nx < len(nb) and 0 <= ny < m and not vis[nx][ny]:
                q.append((nx, ny, dist + 1))
                vis[nx][ny] = 1
    
    # 비교할 때는 dist 값을 사용하지만 return할 때는 빼 주어야 한다
    # 그렇지 않으면 removed에 dist 값까지 들어가 중복된 좌표를 들고 있을 수 있음
    return sorted(res, key=lambda x: (x[2], x[1]))[0][:2] if res else (-1, -1)

n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
enemy = sum(sum(i) for i in board)
ans = 0

for comb in combinations(range(m), 3):
    nb = [[board[i][j] for j in range(m)] for i in range(n)] + [[0] * m]
    # 궁수 위치 표시
    for x in comb:
        nb[-1][x] = 2
    cnt = 0
    e = enemy
    
    while e:
        # 궁수에게 공격당한 적의 위치를 들고 있는 set
        removed = set()
        for x in comb:
            removed.add(bfs(len(nb) - 1, x, nb))
        
        for i, j in removed:
            if (i, j) == (-1, -1):
                continue
            nb[i][j] = 0
            cnt += 1

        # 한 칸씩 내리고 남은 적 수 update
        nb.pop(-2)
        e = sum(sum(i) for i in nb[:-1])
    
    ans = max(cnt, ans)

print(ans)