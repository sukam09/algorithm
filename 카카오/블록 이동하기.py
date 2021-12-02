from collections import deque, defaultdict

def rotate(x, y):
    res = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
    wall = [(x - 1, y + 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y - 1)]
    return res, wall

def solution(board):
    n = len(board)
    q = deque([(0, 0, 0, 1, 0)])
    vis = defaultdict(int)
    vis[(0, 0, 0, 1)] = 1
    mv = [(0, 1, 0, 1), (0, -1, 0, -1), (1, 0, 1, 0), (-1, 0, -1, 0)]
    
    while q:
        x1, y1, x2, y2, ans = q.popleft()

        if (x1, y1) == (n - 1, n - 1) or (x2, y2) == (n - 1, n - 1):
            return ans
        
        for mx1, my1, mx2, my2 in mv:
            nx1, ny1, nx2, ny2 = x1 + mx1, y1 + my1, x2 + mx2, y2 + my2
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n and not board[nx1][ny1] \
                and not board[nx2][ny2] and not vis[(nx1, ny1, nx2, ny2)]:
                q.append((nx1, ny1, nx2, ny2, ans + 1))
                vis[(nx1, ny1, nx2, ny2)] = 1
        
        r1, w1 = rotate(x1, y1)
        r2, w2 = rotate(x2, y2)
        
        nx1, ny1 = x1, y1
        for (nx2, ny2), (wx, wy) in zip(r1, w1):
            if 0 <= nx2 < n and 0 <= ny2 < n and 0 <= wx < n and 0 <= wy < n and not board[nx2][ny2] \
                and not board[wx][wy] and not vis[(nx1, ny1, nx2, ny2)]:
                q.append((nx1, ny1, nx2, ny2, ans + 1))
                vis[(nx1, ny1, nx2, ny2)] = 1
        
        nx1, ny1 = x2, y2
        for (nx2, ny2), (wx, wy) in zip(r2, w2):
            if 0 <= nx2 < n and 0 <= ny2 < n and 0 <= wx < n and 0 <= wy < n and not board[nx2][ny2] \
                and not board[wx][wy] and not vis[(nx1, ny1, nx2, ny2)]:
                q.append((nx1, ny1, nx2, ny2, ans + 1))
                vis[(nx1, ny1, nx2, ny2)] = 1

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))


