def oob(x, y, h, w):
    return x < 0 or x >= h or y < 0 or y >= w

def check(x1, y1, x2, y2, h, w):
    return (oob(x1, y1, h, w) or nb[x1][y1] == '0') and (oob(x2, y2, h, w) or nb[x2][y2] == '0')

def solution(h, w, n, board):
    global nb
    nb = board
    ans = 0
    for i in range(h):
        for j in range(w - n + 1):
            for k in range(n):
                if nb[i][j + k] == '0':
                   break
            else:
                if check(i, j - 1, i, j + n, h, w):
                    ans += 1
    for i in range(h - n + 1):
        for j in range(w):
            for k in range(n):
                if nb[i + k][j] == '0':
                    break
            else:
                if check(i - 1, j, i + n, j, h, w):
                    ans += 1
    for i in range(h - n + 1):
        for j in range(w - n + 1):
            for k in range(n):
                if nb[i + k][j + k] == '0':
                    break
            else:
                if check(i - 1, j - 1, i + n, j + n, h, w):
                    ans += 1
    for i in range(h - n + 1):
        for j in range(n - 1, w):
            for k in range(n):
                if nb[i + k][j - k] == '0':
                    break
            else:
                if check(i - 1, j + 1, i + n, j - n, h, w):
                    ans += 1
    return ans