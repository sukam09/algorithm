from itertools import combinations

def ckcheck(cb, n, relation):
    res = []
    for i in range(n):
        temp = ()
        for j in cb:
            temp += relation[i][j],
        res.append(temp)
    return set(res)

def minimality(cb, n, relation):
    if len(cb) == 1:
        return True
    cnt = 0
    for c in combinations(cb, len(cb) - 1):
        res = ckcheck(c, n, relation)
        if len(res) != n:
            cnt += 1
    return cnt == len(cb)

def solution(relation):
    ans = 0
    n, m = len(relation), len(relation[0])
    for i in range(1, m + 1):
        for cb in combinations(range(m), i):
            res = ckcheck(cb, n, relation)
            if len(res) == n and minimality(cb, n, relation):
                ans += 1
    return ans