from collections import deque


def bfs(n, seat_info):
    q = deque()
    vis = [[0] * n for _ in range(n)]
    for x, y in seat_info:
        vis[x][y] = 1
        q.append((x, y, 0))

    res = []
    dist = 0

    while q:
        x, y, d = q.popleft()
        for nx, ny in (x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y):
            if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny]:
                q.append((nx, ny, d + 1))
                vis[nx][ny] = 1
                if d + 1 > dist:
                    res = [(nx, ny, d + 1)]
                    dist = d + 1
                elif d + 1 == dist:
                    res.append((nx, ny, d + 1))

    res.sort(key=lambda item: (-item[2], item[1], item[0]))
    target = res[0]
    seat_info.append((target[0], target[1]))
    return target, seat_info

def solution(n, k):
    seat_info = [(0, 0)]

    for _ in range(2, k + 1):
        target, seat_info = bfs(n, seat_info)

    x, y, _ = target
    return [x + 1, y + 1]