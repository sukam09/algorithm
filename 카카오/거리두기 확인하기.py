def check(p):
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                for x, y in (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j):
                    if 0 <= x < 5 and 0 <= y < 5 and p[x][y] == 'P':
                        return False
                for x, y in (i - 2, j), (i, j - 2), (i, j + 2), (i + 2, j):
                    if 0 <= x < 5 and 0 <= y < 5 and p[x][y] == 'P' and p[(i + x) // 2][(j + y) // 2] == 'O':
                        return False
                for x, y in (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1):
                    if 0 <= x < 5 and 0 <= y < 5 and p[x][y] == 'P' and (p[x][j] == 'O' or p[i][y] == 'O'):
                        return False
    return True

def solution(places):
    ans = []
    for p in places:
        if check(p):
            ans.append(1)
        else:
            ans.append(0)
    return ans