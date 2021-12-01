from collections import deque

def compress(x, y, l, arr):
    if l == 1:
        res = 'one' if arr[x][y] else 'zero'
        return [(x, y, res)]

    val = sum(arr[i][j] for i in range(x, x + l) for j in range(y, y + l))
    if val == 0:
        return [(x, y, 'zero')]
    elif val == l ** 2:
        return [(x, y, 'one')]
    else:
        return [(x, y, l // 2), (x, y + l // 2, l // 2), (x + l // 2, y, l // 2), (x + l // 2, y + l // 2, l // 2)]

def solution(arr):
    ans = {'zero': 0, 'one': 0}
    q = deque([(0, 0, len(arr))])
    while q:
        x, y, l = q.popleft()
        if l in ans:
            ans[l] += 1
        else:
            q += compress(x, y, l, arr)
    
    return [ans['zero'], ans['one']]