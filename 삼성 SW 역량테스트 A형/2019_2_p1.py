import sys
from collections import deque
input = sys.stdin.readline

def solve(x, d, k, tc):
    for i in range(n):
        if (i + 1) % x != 0: continue
        # 회전
        if d == 0:
            board[i].rotate(k)
        else:
            board[i].rotate(-k)
    erased = set()
    # r이 같을때
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0: continue
            if board[i][j] == board[i][(j - 1 + m) % m]:
                erased.add((i, j))
                erased.add((i, (j - 1 + m) % m))
            if board[i][j] == board[i][(j + 1 + m) % m]:
                erased.add((i, j))
                erased.add((i, (j + 1 + m) % m))
    # m이 값을때
    # r은 m과 다르게 circular 구조가 아님
    for j in range(m):
        for i in range(n):
            if board[i][j] == 0: continue
            if i == 0:
                if board[i][j] == board[i + 1][j]:
                    erased.add((i, j))
                    erased.add((i + 1, j))
            elif i == n - 1:
                if board[i][j] == board[i - 1][j]:
                    erased.add((i, j))
                    erased.add((i - 1, j))
            else:
                if board[i][j] == board[i - 1][j]:
                    erased.add((i, j))
                    erased.add((i - 1, j))
                if board[i][j] == board[i + 1][j]:
                    erased.add((i, j))
                    erased.add((i + 1, j))
    for x, y in erased: board[x][y] = 0
    # 정규화
    tot = 0
    num = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0: continue
            tot += board[i][j]
            num += 1
    if len(erased) == 0:
        avg = tot // num
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0: continue
                if board[i][j] > avg:
                    board[i][j] -= 1
                elif board[i][j] < avg:
                    board[i][j] += 1

n, m, q = map(int, input().split())
board = [] # 0-index
for _ in range(n):
    circle = deque(map(int, input().split()))
    board.append(circle)
for tc in range(q):
    x, d, k = map(int, input().split())
    solve(x, d, k, tc)
ans = 0
for i in range(n):
    for j in range(m):
        ans += board[i][j]
print(ans)