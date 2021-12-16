from math import ceil
from collections import deque

def solution(progresses, speeds):
    day = [ceil((100-x) / y) for x, y in zip(progresses, speeds)]
    Q = deque(day)
    cur = 1
    ans = []
    while Q:
        cnt = 0
        while Q and Q[0] <= cur: 
            Q.popleft()
            cnt += 1
        if cnt:
            ans.append(cnt)
        cur += 1
    return ans