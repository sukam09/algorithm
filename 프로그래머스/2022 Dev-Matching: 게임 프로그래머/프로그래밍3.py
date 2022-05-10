def check(a):
    return a == [[1, 1, 2, 2], [1, 1, 2, 2], [2, 2, 1, 1], [2, 2, 1, 1]]

def row_rotate(row, k, a):
    tmp = []
    cnt = 0
    for i in range(k, 4):
        tmp.append(a[row][i])
        cnt += 1
    for i in range(cnt):
        tmp.append(a[row][i])
    a[row] = tmp

def col_rotate(col, k, a):
    tmp = []
    cnt = 0
    for i in range(k, 4):
        tmp.append(a[i][col])
        cnt += 1
    for i in range(cnt):
        tmp.append(a[i][col])
    for i in range(4):
        a[i][col] = tmp[i]

def solve(cnt, grid):
    print(grid)
    global ans
    if cnt > ans:
        return
    if check(grid) and ans < cnt:
        ans = cnt
        return
    for i in range(4):
        for j in range(1, 4):
            row_rotate(i, j, grid)
            solve(cnt + 1, grid)
            row_rotate(i, 4 - j, grid)
    for i in range(4):
        for j in range(1, 4):
            col_rotate(i, j, grid)
            solve(cnt + 1, grid)
            col_rotate(i, 4 - j, grid)

def solution(grid):
    global ans
    ans = 1
    solve(0, grid)
    return ans