from collections import deque

def bfs(board, start_dir):
    n = len(board)
    q = deque([(0, 0, start_dir, 0)])
    cost = [[float('inf')] * n for _ in range(n)]
    cost[0][0] = 0
    dir = ['U', 'L', 'R', 'D']

    while q:
        x, y, d, c = q.popleft()

        for i, (nx, ny) in enumerate([(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]):
            next = 600 if dir[i] != d else 100
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny] and c + next < cost[nx][ny]:
                q.append((nx, ny, dir[i], c + next))
                cost[nx][ny] = c + next
                
    return cost[n - 1][n - 1]

def solution(board):
    return min(bfs(board, 'R'), bfs(board, 'D'))