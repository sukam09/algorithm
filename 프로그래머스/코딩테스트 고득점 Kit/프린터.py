from collections import deque

def solution(priorities, location):
    Q = deque(enumerate(priorities))
    ans = 1
    while len(Q) > 1:
        r = [x[1] for x in list(Q)[1:]]
        if Q[0][1] >= max(r):
            l = Q.popleft()[0]
            if l == location:
                return ans
            else:
                ans += 1
        else:
            Q.rotate(-1)
    return ans