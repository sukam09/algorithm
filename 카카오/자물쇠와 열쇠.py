def count(lock, n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not lock[i][j]:
                cnt += 1
    return cnt

def rotate(key, m):
    res = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            res[i][j] = key[m - 1 - j][i]
    return res

def search(key, lock, m, n, key_groove):
    for i in range(1 - m, 2 * m - 1):
        for j in range(1 - m, 2 * m - 1):
            if check(key, lock, i, j, m, n, key_groove):
                return True
    return False

def check(key, lock, x, y, m, n, key_groove):
    cnt = 0
    for i in range(m):
        for j in range(m):
            if 0 <= x + i < n and 0 <= y + j < n:
                if key[i][j] == 1 and lock[x + i][y + j] == 0:
                    cnt += 1
                if key[i][j] == lock[x + i][y + j] == 1:
                    return False
    return cnt == key_groove

def solution(key, lock):
    m, n = len(key), len(lock)
    key_groove = count(lock, n)

    for _ in range(4):
        ans = search(key, lock, m, n, key_groove)
        if ans:
            return True
        key = rotate(key, m)
    
    return False