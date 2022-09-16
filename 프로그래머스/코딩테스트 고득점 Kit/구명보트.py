from collections import Counter, deque
from math import ceil

def solution(people, limit):
    ans = 0
    c = Counter(people)
    w = deque(sorted(c.keys(), reverse=True))
    while len(w) > 1:
        if c[w[0]] == 0:
            w.popleft()
        else:
            target = w[0]
            if target * 2 <= limit:
                return ans + ceil(sum(c.values()) / 2)
            pair = False
            for x in list(w)[1:]:
                if c[x] and target+x <= limit:
                    res = min(c[target], c[x])
                    ans += res
                    c[target] -= res
                    c[x] -= res
                    pair = True
                    break
            if not pair:
                ans += c[target]
                c[target] = 0
    if w[0]*2 <= limit:
        return ans + ceil(c[w[0]] / 2)
    else:
        return ans + c[w[0]]