from collections import deque

def rotate(x, y, nx, ny, arr):
    q = deque()
    for i in range(y, ny + 1):
        q.append(arr[x][i])
    for i in range(x + 1, nx + 1):
        q.append(arr[i][ny])
    for i in range(ny - 1, y - 1, -1):
        q.append(arr[nx][i])
    for i in range(nx - 1, x, -1):
        q.append(arr[i][y])
    
    q.rotate(1)
    minval = min(q)

    for i in range(y, ny + 1):
        arr[x][i] = q.popleft()
    for i in range(x + 1, nx + 1):
        arr[i][ny] = q.popleft()
    for i in range(ny - 1, y - 1, -1):
        arr[nx][i] = q.popleft()
    for i in range(nx - 1, x, -1):
        arr[i][y] = q.popleft()
    
    return arr, minval

def solution(rows, columns, queries):
    arr = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = i * columns + j + 1       

    ans = []
    for query in queries:
        x, y, nx, ny = query
        arr, minval = rotate(x - 1, y - 1, nx - 1, ny - 1, arr)
        ans.append(minval)
    
    return ans