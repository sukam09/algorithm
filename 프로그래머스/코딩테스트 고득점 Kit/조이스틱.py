from collections import deque

def solution(name):
    ans = 0
    ans += min(ord(name[0])-ord('A'), 26+ord('A')-ord(name[0]))
    na = deque([i for i, x in enumerate(name) if i and x != 'A'])
    cur = 0
    while len(na) > 1:
        i, j = na[0], na[-1]
        res1 = min(abs(i-cur), len(name)+cur-i)
        res2 = min(abs(j-cur), len(name)+cur-j)
        if res1 <= res2:
            pos = i
            na.popleft()
            res = res1
        else:
            pos = j
            na.pop()
            res = res2
        target = name[pos]
        ans += res
        ans += min(ord(target) - ord('A'), 26 + ord('A') - ord(target))
        cur = pos
    if na:
        pos = na[0]
        target = name[pos]
        ans += min(abs(pos-cur), len(name)+cur-pos)
        ans += min(ord(target) - ord('A'), 26 + ord('A') - ord(target))
    return ans