from collections import deque
input = __import__('sys').stdin.readline

def solve():
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == 'S':
                    z, x, y = i, j, k
                    break
    
    vis = [[[0] * c for _ in range(r)] for _ in range(l)]
    vis[z][x][y] = 1
    q = deque([(z, x, y, 0)])
    while q:
        z, x, y, ans = q.popleft()
        if building[z][x][y] == 'E':
            print(f"Escaped in {ans} minute(s).")
            return
        for d in range(6):
            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]
            if oob(nz, nx, ny) or building[nz][nx][ny] == '#' or vis[nz][nx][ny]:
                continue
            vis[nz][nx][ny] = 1
            q.append((nz, nx, ny, ans + 1))
    print("Trapped!")

dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, 0, -1, 0]
dy = [0, 0, 0, 1, 0, -1]
oob = lambda z, x, y: z < 0 or z >= l or x < 0 or x >= r or y < 0 or y >= c
while True:
    l, r, c = map(int, input().split())
    if l == r == c == 0:
        break
    building = []
    for _ in range(l):
        board = [input().rstrip() for _ in range(r)]
        building.append(board)
        input()
    solve()