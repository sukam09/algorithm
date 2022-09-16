from collections import deque
from bisect import bisect_right

def get_s(t):
    h, m = t.split(':')
    return 60 * int(h) + int(m)

def search(q, now, m):
    for i in range(now, q[0] - 1, -1):
        target = bisect_right(q, i)
        if target < m:
            return i
    return q[0] - 1

def solution(n, t, m, timetable):
    q = deque(sorted(map(get_s, timetable)))
    now = get_s('09:00')
    
    for _ in range(n - 1):
        cnt = 0
        while q and q[0] <= now and cnt < m:
            q.popleft()
            cnt += 1
        now += t
    
    q = [s for s in q if s <= now]
    if not q:
        ans = now
    else:
        ans = search(q, now, m)

    HH = str(ans // 60).zfill(2)
    MM = str(ans % 60).zfill(2)
    
    return '%s:%s' % (HH, MM)