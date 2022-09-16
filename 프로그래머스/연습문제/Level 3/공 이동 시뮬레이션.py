def solution(n, m, x, y, queries):
    # 현재가 가장 마지막 쿼리이고 (x, y)에 모든 공이 있다고 가정.
    sx, ex = x, x
    sy, ey = y, y

    # 쿼리를 역으로 순회하면서 공의 위치가 될 수 있는 후보군을 직사각형의 형태로 구성.
    for i in range(len(queries) - 1, -1, -1):
        cmd, d = queries[i]
        
        # 0, 1, 2, 3 -> 좌, 우, 상, 하
        # 이전 step에서 어떤 범위의 있는 공들이 현재 위치로 올 수 있는가를 역으로 추적.
        if cmd == 0:
            if sy:
                sy += d
            ey = min(ey + d, m - 1)
        elif cmd == 1:
            if ey != m - 1:
                ey -= d
            sy = max(sy - d, 0)
        elif cmd == 2:
            if sx:
                sx += d
            ex = min(ex + d, n - 1)
        else:
            if ex != n - 1:
                ex -= d
            sx = max(sx - d, 0)
        
        # 다음 조건을 만족할 경우 이전 step에서 어떻게 해도 현재 step에 도달할 수 없음이 보장됨.
        if sx > n - 1 or ex < 0 or sy > m - 1 or ey < 0:
            return 0

    return (ex - sx + 1) * (ey - sy + 1)