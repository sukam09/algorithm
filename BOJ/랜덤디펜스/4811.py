import sys
input = sys.stdin.readline

# d[h][w]: 알약 반 조각이 h개, 알약 한 조각이 w개 존재할 때 나올 수 있는 문자열의 개수
def dfs(h, w):
    global ans
    if d[h][w]:
        return d[h][w]
    a = b = 0
    if h > 0:
        a = dfs(h - 1, w)
    if w > 0:
        b = dfs(h + 1, w - 1)
    d[h][w] = a + b
    return d[h][w]

while 1:
    n = int(input())
    if n == 0:
        break
    ans = 0
    h = 1
    w = n - 1
    d = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        d[i][0] = 1
    print(dfs(h, w))