from collections import deque, defaultdict
from itertools import permutations

def ctrlmove(x, y, dx, dy):
    while True:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx > 3 or ny < 0 or ny > 3:
            return x, y
        if nb[nx][ny]:
            return nx, ny
        x, y = nx, ny

def bfs(x1, y1, x2, y2):
    vis = [[0] * 4 for _ in range(4)]
    vis[x1][y1] = 1
    q = deque([(x1, y1, 0)])
    while q:
        x, y, d = q.popleft()
        if (x, y) == (x2, y2):
            return d
        
        for nx, ny in (x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y):
            if 0 <= nx < 4 and 0 <= ny < 4 and not vis[nx][ny]:
                q.append((nx, ny, d + 1))
                vis[nx][ny] = 1
        
        for nx, ny in ctrlmove(x, y, -1, 0), ctrlmove(x, y, 0, -1), \
                        ctrlmove(x, y, 0, 1), ctrlmove(x, y, 1, 0):
            if 0 <= nx < 4 and 0 <= ny < 4 and not vis[nx][ny]:
                q.append((nx, ny, d + 1))
                vis[nx][ny] = 1

def remove(card, nb):
    for c in card:
        x, y = c
        nb[x][y] = 0

def restore(card, nb, target):
    for c in card:
        x, y = c
        nb[x][y] = target

def backtrack(x, y, cnt, order, res):
    global ans

    if cnt == num:
        ans = min(res, ans)
        return

    target = orders[order][cnt]
    card = card_loc[target]

    lx, ly = card[0][0], card[0][1]
    rx, ry = card[1][0], card[1][1]

    lr = bfs(x, y, lx, ly) + bfs(lx, ly, rx, ry) + 2
    rr = bfs(x, y, rx, ry) + bfs(rx, ry, lx, ly) + 2

    remove(card, nb)
    backtrack(rx, ry, cnt + 1, order, res + lr)
    restore(card, nb, target)

    remove(card, nb)
    backtrack(lx, ly, cnt + 1, order, res + rr)
    restore(card, nb, target)

def solution(board, r, c):
    global nb, num, ans, orders, card_loc

    cards = set()
    card_loc = defaultdict(list)
    
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                card_loc[board[i][j]].append((i, j))
                cards.add(board[i][j])
    
    nb = [[board[i][j] for j in range(4)] for i in range(4)]
    num = len(cards)
    ans = float('inf')
    orders = list(permutations(cards, num))

    for i in range(len(orders)):
        backtrack(r, c, 0, i, 0)
    
    return ans