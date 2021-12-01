from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    od = {}
    for o in orders:
        od[o] = defaultdict(int)
        for c in o:
            od[o][c] = 1
    ans = []
    for c in course:
        candidate = []
        for o in orders:
            candidate += list(combinations(o, c))
        candidate = set(candidate)
        res = []
        maxval = 0
        for cb in candidate:
            cnt = 0
            for o in orders:
                n = 0
                for x in cb:
                    n += od[o][x]
                if n == c:
                    cnt += 1
            if cnt > maxval:
                maxval = cnt
                res = [(cb, cnt)]
            elif cnt == maxval:
                res.append((cb, cnt))
        res = set([''.join(sorted(r[0])) for r in res if r[1] == maxval if r[1] >= 2])
        ans += res
    return sorted(ans)