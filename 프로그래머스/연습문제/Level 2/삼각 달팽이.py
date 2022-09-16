def snail(n, i, cnt, arr):
    for j in range(2 * i, n - i):
        arr[j][i] = cnt
        cnt += 1
    
    for j in range(i + 1, n - 2 * i):
        arr[-(i + 1)][j] = cnt
        cnt += 1

    for j in range(n - i - 2, 2 * i, -1):
        arr[j][-(i + 1)] = cnt
        cnt += 1
    
    return cnt

def solution(n):
    arr = [[0] * i for i in range(1, n + 1)]
    cnt = 1

    for i in range(n // 3 + 1):
        cnt = snail(n, i, cnt, arr)
    
    ans = []
    for row in arr:
        ans += row
    
    return ans